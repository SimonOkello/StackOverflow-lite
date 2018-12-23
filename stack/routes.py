from flask import url_for, render_template
from stack import app
#from stack.forms import RegistrationForm, LoginForm

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")