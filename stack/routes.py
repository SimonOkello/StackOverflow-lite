from flask import url_for, render_template
from stack import app
from stack.forms import RegistrationForm, LoginForm

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login")
def login():
    form = LoginForm()
    return render_template("login.html", title = "Login", form = form)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template("register.html", title = "Register", form = form)