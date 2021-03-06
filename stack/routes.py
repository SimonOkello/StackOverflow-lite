from flask import render_template, url_for
from stack import app
from stack.forms import LoginForm, RegistrationForm

questions = [
    {
        "id": 1,
        "title": "How does one install Flask in Virtual Environment",
        "content": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. ",
        "author": "SimonOkello",
        "date_posted": "25-12-2018"
    },
    {
        "id": 2,
        "title": "How does one install SqlAlchemy in Virtual Environment",
        "content": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. ",
        "author": "Enock",
        "date_posted": "24-12-2018"
    },
    {
        "id": 3,
        "title": "How does one install Pylint in Virtual Environment",
        "content": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. ",
        "author": "Jeff",
        "date_posted": "23-12-2018"
    }
]


@app.route("/")
def home():
    return render_template("index.html", title="HomePage", questions=questions)


@app.route("/login")
def login():
    form = LoginForm()
    return render_template("login.html", title="Login", form=form)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template("register.html", title="Register", form=form)


@app.route("/question/<string:id>/")
def question(id):
    return render_template("question.html", title="question", id=id)
