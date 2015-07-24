__author__ = 'gherero'
from flask import render_template
from app import app
from .forms import LoginForm
from .forms import NameForm
from flask import request



@app.route("/log", methods=['GET','POST'])
def hello():
    form = LoginForm()
    name=form.name.data
    login=form.login.data
    passwd=form.passwrd.data
    print (login)
    return render_template('test.html', form=form)

@app.route('/', methods=['GET', 'POST'])
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
        print(name)
    return render_template('test.html', form=form, name=name)