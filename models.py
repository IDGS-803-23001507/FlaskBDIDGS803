import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Alumnos(db.Model):
    __tablename__ = 'alumnos'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    apellidos = db.Column(db.String(50))
    email = db.Column(db.String(50))
    telefono = db.Column(db.String(50))
    created_date = db.Column(db.DateTime, default=datetime.datetime.now)
    
    cursos = db.relationship(
        'Cursos',
        secondary='inscripciones',   
        back_populates='alumnos'
    )


class Maestros(db.Model):
    __tablename__ = "maestros"
    matricula = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    apellidos = db.Column(db.String(50))
    especialidad = db.Column(db.String(50))
    email = db.Column(db.String(50))
    
    cursos = db.relationship(
        'Cursos',
        back_populates='maestro'
    )


class Cursos(db.Model):
    __tablename__ = "cursos"
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(150))
    descripcion = db.Column(db.Text)
    
    maestros_id = db.Column(
        db.Integer,
        db.ForeignKey('maestros.matricula'),
        nullable=False
    )
    
    maestro = db.relationship('Maestros', back_populates='cursos')

    alumnos = db.relationship(
        'Alumnos',
        secondary='inscripciones',
        back_populates='cursos'
    )


class Inscripciones(db.Model):
    __tablename__ = "inscripciones"

    id = db.Column(db.Integer, primary_key=True)

    alumno_id = db.Column(
        db.Integer,
        db.ForeignKey('alumnos.id'),
        nullable=False
    )

    cursos_id = db.Column(
        db.Integer,
        db.ForeignKey('cursos.id'),
        nullable=False
    )

    fecha_inscripcion = db.Column(
        db.DateTime,
        server_default=db.func.now()
    )

    __table_args__ = (
        db.UniqueConstraint('alumno_id', 'cursos_id', name='uq_alumno_cursos'),
    )