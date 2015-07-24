__author__ = 'gherero'
from flask import render_template
from app import app
from .forms import LoginForm
from flask import request



@app.route("/log", methods=['GET','POST'])
def hello():
    form = LoginForm()
    if form.validate_on_submit():
        result = form.TestString.data
        print (result)

    else:
        result = 'not submitted'
    return render_template('test.html', form=form, result=result)