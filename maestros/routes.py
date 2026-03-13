from . import maestros
from flask import Flask, render_template, request, redirect, url_for
from flask import flash
from flask_wtf.csrf import CSRFProtect
from flask import g
from models import db
from models import Alumnos, Maestros
from config import DevelopEmConfig
import forms
from flask_migrate import Migrate

@maestros.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@maestros.route("/maestros")
def index_maestros():
    create_form = forms.MaestrosForm(request.form)
    lista_maestros = Maestros.query.all()
    return render_template("maestros/indexMaestros.html", form=create_form, maestros=lista_maestros)

@maestros.route("/detalles_maestro")
def detalles_maestros():
    matricula = request.args.get('matricula')
    maest = Maestros.query.get_or_404(matricula)
    return render_template("maestros/detalles_maestro.html", maest=maest)

@maestros.route("/insertMestros", methods=["GET", "POST"])
def insert_maestros():
    create_form = forms.MaestrosForm(request.form)

    if request.method == "POST":

        maestro_existente = Maestros.query.filter_by(matricula=create_form.matricula.data).first()

        if maestro_existente:
            flash("Ya existe un maestro con esa matrícula")
            return redirect(url_for('maestros.insert_maestros'))

        Mast = Maestros(
            matricula=create_form.matricula.data,
            nombre=create_form.nombre.data,
            apellidos=create_form.apellidos.data,
            especialidad=create_form.especialidad.data,
            email=create_form.email.data
        )

        db.session.add(Mast)
        db.session.commit()

        return redirect(url_for('maestros.index_maestros'))

    return render_template("maestros/Maestros_insert.html", form=create_form)
@maestros.route("/actualizar_maestros", methods=["GET", "POST"])
def actualizar_maestros():
    create_form = forms.MaestrosForm(request.form)
    if request.method=="GET":
        matricula = request.args.get('matricula')
        maest1 = db.session.query(Maestros).filter(Maestros.matricula == matricula).first()
        create_form.matricula.data = request.args.get('matricula')
        create_form.nombre.data  = maest1.nombre 
        create_form.apellidos.data  = maest1.apellidos
        create_form.especialidad.data  = maest1.especialidad
        create_form.email.data  = maest1.email
          
    if request.method=="POST":
        matricula = request.args.get('matricula')
        maest1 = db.session.query(Maestros).filter(Maestros.matricula == matricula).first()        
        maest1.nombre = create_form.nombre.data  
        maest1.apellidos = create_form.apellidos.data  
        maest1.especialidad = create_form.especialidad.data 
        maest1.email = create_form.email.data    
        db.session.add(maest1)
        db.session.commit()
        return redirect(url_for('maestros.index_maestros'))       
    return render_template("maestros/actualizar_maestros.html", form = create_form) 

@maestros.route("/eliminar_maestros", methods=["GET", "POST"])
def eliminar_maestros():
    create_form = forms.MaestrosForm(request.form)
    if request.method=="GET":
        matricula = request.args.get('matricula')
        maest1 = db.session.query(Maestros).filter(Maestros.matricula == matricula).first()
        create_form.matricula.data = request.args.get('matricula')
        create_form.nombre.data  = maest1.nombre 
        create_form.apellidos.data  = maest1.apellidos
        create_form.especialidad.data  = maest1.especialidad
        create_form.email.data  = maest1.email
          
    if request.method=="POST":
        matricula = request.args.get('matricula')
        maest1 = db.session.query(Maestros).filter(Maestros.matricula == matricula).first()        
        maest1.nombre = create_form.nombre.data  
        maest1.apellidos = create_form.apellidos.data  
        maest1.especialidad = create_form.especialidad.data 
        maest1.email = create_form.email.data    
        db.session.delete(maest1)
        db.session.commit()
        return redirect(url_for('maestros.index_maestros'))     
    return render_template("maestros/eliminar_maestros.html", form = create_form) 