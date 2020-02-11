from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField
frok wtforms.validators import DataRequired,Length,Email,EqualTo

class RegistrationForm(FlaskForm):
    username = StringField('username',validators=[DataRequired(),Length(min=2,max=20)])
    email = StringField('email',validators=[DataRequired(),Email()])
    password = PasswordField('password',validators=[DataRequired()])
    Confirmpassword = PasswordField('Confirmpassword',validators=[DataRequired(),])