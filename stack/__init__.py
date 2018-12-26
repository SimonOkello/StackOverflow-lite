from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


from stack.forms import LoginForm, RegistrationForm

app = Flask(__name__)

app.config["SECRET_KEY"] = "f43f7d7a100fe149d743fc800901f7df"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from stack import routes, models


