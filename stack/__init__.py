from flask import Flask
from forms import RegistrationForm, LoginForm



app  =  Flask(__name__)

app.config["SECRET_KEY"] = "f43f7d7a100fe149d743fc800901f7df"

from stack import routes