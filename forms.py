from wtforms import Form
from wtforms import StringField, IntegerField, PasswordField, DateField
from wtforms import EmailField, SelectField
from wtforms import validators
from wtforms.validators import DataRequired

class UserForm(Form):
    
    id = IntegerField('id')
                            
    nombre = StringField("nombre", [
        validators.DataRequired(message = "el campo es requerido"),
        validators.length(min=4, max= 50, message = " ingresa nombre valido"),
       
    ])
    apellidos= StringField("apellidos", [
         validators.DataRequired(message = "el campo es requerido"),
    ])
    
    email = StringField("email",[
         validators.DataRequired(message = "el campo es requerido"),
     ])
    
    telefono = StringField("telefono",[
         validators.DataRequired(message = "el campo es requerido"),
     ])
    
    
class MaestrosForm(Form):
    
    matricula = IntegerField('id')
                            
    nombre = StringField("nombre", [
        validators.DataRequired(message = "el campo es requerido"),
        validators.length(min=4, max= 50, message = " ingresa nombre valido"),
       
    ])
    
    apellidos= StringField("apellidos", [
         validators.DataRequired(message = "el campo es requerido"),
    ])
    
    especialidad = StringField("telefono",[
         validators.DataRequired(message = "el campo es requerido"),
     ])
    
    email = StringField("email",[
         validators.DataRequired(message = "el campo es requerido"),
     ])
    
    
class CursosForm(Form):
    
    id = IntegerField('id')
                            
    nombre = StringField("nombre", [
        validators.DataRequired(message = "el campo es requerido"),
        validators.length(min=4, max= 50, message = " ingresa nombre valido"),
       
    ])
    
    descripcion= StringField("descripcion", [
         validators.DataRequired(message = "el campo es requerido"),
    ])
    
    maestro_id = SelectField('Profesor',
        coerce=int,
        validators=[DataRequired()]
    )
    
class InscripcionesForm(Form):
    
    id = IntegerField('id')
                            
    alumno_id = SelectField('Alumno', 
        coerce=int, validators=[DataRequired()])
    
    cursos_id = SelectField('Curso', 
        coerce=int, validators=[DataRequired()])

    fecha_inscripcion = DateField('fecha_inscripcion')