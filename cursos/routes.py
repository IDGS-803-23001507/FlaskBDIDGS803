from . import cursos
from flask import Flask, render_template, request, redirect, url_for
from flask import flash
from flask_wtf.csrf import CSRFProtect
from flask import g
from models import db
from models import Alumnos, Maestros, Cursos
from config import DevelopEmConfig
import forms
from forms import InscripcionesForm
from flask_migrate import Migrate

@cursos.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404



@cursos.route("/cursos")
def indexCursos():
    create_form = forms.CursosForm(request.form)
    cursos = Cursos.query.all()
    return render_template("cursos/indexCursos.html", form=create_form, cursos= cursos)


@cursos.route("/insertCursos", methods=["GET", "POST"])
def insertCursos():

    create_form = forms.CursosForm(request.form)

    maestros = Maestros.query.all()
    create_form.maestro_id.choices = [
        (m.matricula, f"{m.nombre}") for m in maestros
    ]

    if request.method == "POST" and create_form.validate():

        cursos = Cursos(
            nombre=create_form.nombre.data,
            descripcion=create_form.descripcion.data,
            maestros_id=create_form.maestro_id.data
        )

        db.session.add(cursos)
        db.session.commit()

        return redirect(url_for("index"))

    return render_template("cursos/cursos.html", form=create_form)
 
@cursos.route("/detallesCursos")
def detallesCursos():
    id = request.args.get('id')
    curs = Cursos.query.get_or_404(id)
    return render_template("cursos/detallesCursos.html", curs = curs)

@cursos.route("/modificarCursos", methods=["GET", "POST"])
def modificarCursos():
    create_form = forms.CursosForm(request.form)

    maestros = Maestros.query.all()
    create_form.maestro_id.choices = [
        (m.matricula, f"{m.nombre}") for m in maestros
    ]
    
    if request.method=="GET":
        id = request.args.get('id')
        curs1 = db.session.query(Cursos).filter(Cursos.id == id).first()
        create_form.id.data = request.args.get('id')
        create_form.nombre.data  = curs1.nombre 
        create_form.descripcion.data  = curs1.descripcion
        create_form.maestro_id.data  = curs1.maestros_id
        
    if request.method=="POST":
        id = request.args.get('id')
        curs1 = db.session.query(Cursos).filter(Cursos.id == id).first()        
        curs1.nombre = create_form.nombre.data  
        curs1.descripcion = create_form.descripcion.data  
        curs1.maestros_id = create_form.maestro_id.data    
        db.session.add(curs1)
        db.session.commit()
        return redirect(url_for("index"))     
    return render_template("cursos/modificarCursos.html", form = create_form) 

@cursos.route("/eliminarCursos", methods=["GET", "POST"])
def eliminarCursos():
    create_form = forms.CursosForm(request.form)
    
    maestros = Maestros.query.all()
    create_form.maestro_id.choices = [
        (m.matricula, f"{m.nombre}") for m in maestros
    ]
    
    if request.method=="GET":
        id = request.args.get('id')
        curs1 = db.session.query(Cursos).filter(Cursos.id == id).first()
        create_form.id.data = request.args.get('id')
        create_form.nombre.data  = curs1.nombre 
        create_form.descripcion.data  = curs1.descripcion
        create_form.maestro_id.data  = curs1.maestros_id
        
    if request.method=="POST":
        id = request.args.get('id')
        curs1 = db.session.query(Cursos).filter(Cursos.id == id).first()        
        curs1.nombre = create_form.nombre.data  
        curs1.descripcion = create_form.descripcion.data  
        curs1.maestros_id = create_form.maestro_id.data    
        db.session.delete(curs1)
        db.session.commit()
        return redirect(url_for("index"))     
    return render_template("cursos/eliminarCursos.html", form = create_form) 

@cursos.route("/inscribir", methods=["GET", "POST"])
def inscribir_alumno():
    form = InscripcionesForm(request.form)

    alumnos = Alumnos.query.all()
    cursos = Cursos.query.all()

    form.alumno_id.choices = [(a.id, f"{a.nombre} {a.apellidos}") for a in alumnos]
    form.cursos_id.choices = [(c.id, c.nombre) for c in cursos]

    if request.method == "POST" and form.validate():
     
        existing = Inscripciones.query.filter_by(
            alumno_id=form.alumno_id.data,
            cursos_id=form.cursos_id.data
        ).first()

        if not existing:
            inscripcion = Inscripciones(
                alumno_id=form.alumno_id.data,
                cursos_id=form.cursos_id.data
            )
            db.session.add(inscripcion)
            db.session.commit()

        return redirect(url_for("index"))
    return render_template("alumnos/inscripciones.html", form=form)