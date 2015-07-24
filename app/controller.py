__author__ = 'gherero'
from flask import render_template
from app import app
from .forms import LoginForm
from flask import request



@app.route("/log", methods=['GET','POST'])
def hello():
    form = LoginForm()
    surname = form.surname.data
    name = form.name.data
    meddle_name=form.Middle_name.data
    internet=form.internet.data
    mail=form.mail.data
    delo=form.delo.data
    print (name)
    return render_template('test.html', form=form, result=1)