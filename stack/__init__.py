from flask import Flask
from flask_sqlalchemy import SQLAlchemy


from stack.forms import LoginForm, RegistrationForm

app = Flask(__name__)

app.config["SECRET_KEY"] = "f43f7d7a100fe149d743fc800901f7df"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
db = SQLAlchemy(app)

from stack import routes


