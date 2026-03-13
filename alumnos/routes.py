from . import alumnos
from flask import Flask, render_template, request, redirect, url_for
from flask import flash
from flask_wtf.csrf import CSRFProtect
from flask import g
from models import db
from models import Alumnos, Maestros, Cursos, Inscripciones
from config import DevelopEmConfig
import forms
from forms import InscripcionesForm
from flask_migrate import Migrate

@alumnos.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@alumnos.route("/inscribir", methods=["GET", "POST"])
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

@alumnos.route("/alumnos")
def indexAlumnos():
    create_form = forms.UserForm(request.form)
    alumnos = Alumnos.query.all()
    return render_template("alumnos/indexAlumnos.html", form=create_form, alumnos=alumnos)

@alumnos.route("/registrarAlumnos", methods=["GET", "POST"])
def insertAlumnos():
     create_form = forms.UserForm(request.form)
     if request.method=="POST":
         alum= Alumnos(nombre = create_form.nombre.data,
                       apellidos = create_form.apellidos.data,
                       email =create_form.email.data,
                       telefono =create_form.telefono.data)
         
         db.session.add(alum)
         db.session.commit()
         return redirect(url_for("index"))
     return render_template("alumnos/alumnos.html", form = create_form)
 
@alumnos.route("/detalles")
def detallesAlumnos():
    id = request.args.get('id')
    alum = Alumnos.query.get_or_404(id)
    return render_template("alumnos/detalles.html", alum=alum)

@alumnos.route("/modificar", methods=["GET", "POST"])
def modificar():
    create_form = forms.UserForm(request.form)
    if request.method=="GET":
        id = request.args.get('id')
        alum1 = db.session.query(Alumnos).filter(Alumnos.id == id).first()
        create_form.id.data = request.args.get('id')
        create_form.nombre.data  = alum1.nombre 
        create_form.apellidos.data  = alum1.apellidos
        create_form.email.data  = alum1.email
        create_form.telefono.data  = alum1.telefono
        
    if request.method=="POST":
        id = create_form.id.data
        alum1 = db.session.query(Alumnos).filter(Alumnos.id == id).first()        
        alum1.nombre = create_form.nombre.data  
        alum1.apellidos = create_form.apellidos.data  
        alum1.email = create_form.email.data   
        alum1.telefono = create_form.telefono.data  
        db.session.add(alum1)
        db.session.commit()
        return redirect(url_for("index"))     
    return render_template("alumnos/modificar.html", form = create_form) 

@alumnos.route("/eliminar", methods=["GET", "POST"])
def eliminar():
    create_form = forms.UserForm(request.form)
    if request.method=="GET":
        id = request.args.get('id')
        alum1 = db.session.query(Alumnos).filter(Alumnos.id == id).first()
        create_form.id.data = request.args.get('id')
        create_form.nombre.data  = alum1.nombre 
        create_form.apellidos.data  = alum1.apellidos
        create_form.email.data  = alum1.email
        
    if request.method=="POST":
        id = request.args.get('id')
        alum1 = db.session.query(Alumnos).filter(Alumnos.id == id).first()        
        alum1.nombre = create_form.nombre.data  
        alum1.apellidos = create_form.apellidos.data  
        alum1.email = create_form.email.data    
        db.session.delete(alum1)
        db.session.commit()
        return redirect(url_for("index"))     
    return render_template("alumnos/eliminar.html", form = create_form) 
