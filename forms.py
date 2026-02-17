from wtforms import Form
from wtforms import StringField, IntegerField, PasswordField
from wtforms import EmailField
from wtforms import validators

class UserForm(Form):
    
    id = IntegerField('id')
                            
    nombre = StringField("nombre", [
        validators.DataRequired(message = "el campo es requerido"),
        validators.length(min=4, max= 10, message = " ingresa nombre valido"),
       
    ])
    apaterno= StringField("apaterno", [
         validators.DataRequired(message = "el campo es requerido"),
    ])
    
    email = StringField("email",[
         validators.DataRequired(message = "el campo es requerido"),
     ])
    