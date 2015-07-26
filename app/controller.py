__author__ = 'gherero'
from flask import render_template, session,redirect,url_for
from app import app
from .forms import LoginForm
from .forms import NameForm
from flask import request



@app.route("/log", methods=['GET','POST'])
def hello():
    #form = LoginForm()
    #name=request.form['login']
    #login=form.login.data
    #passwd=form.passwrd.data
    if request.method == 'POST':
        print(request.form['username'])
    #return 'login'
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        print(request.form['username'])
    return render_template('test.html')