from flask import url_for, render_template
from stack import app
from stack.forms import RegistrationForm, LoginForm

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")