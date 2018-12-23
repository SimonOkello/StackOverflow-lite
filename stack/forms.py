from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, 


class Registration(FlaskForm):
    username = StringField("Username", validators = [DataRequired(), Length(min = 5, max= 20)])
    email = StringField("Email", validators = [DataRequired(), Email])
    password = PasswordField("Password", validators = [DataRequired(), Length(min = 5 max = 15)])
    Confirm_password = PasswordField("Confirm_Password", validators = [DataRequired(), EqualTo("password")])
    submit = SubmitField("Sign Up")

class Login(FlaskForm):
    email = StringField("Email", validators = [DataRequired(), Email])
    password = PasswordField("Password", validators = [DataRequired(), Length(min = 5 max = 15)])
    submit = SubmitField("Sign Up")

