__author__ = 'gherero'
from flask import render_template, session,redirect,url_for
from app import app
from flask import request
#from .forms import LoginForm
#from .forms import NameForm


@app.route("/log", methods=['GET','POST'])
def hello():
    if request.method == 'POST':
        print(request.form['login'])
        print(request.form['password'])
    #return 'login'
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        print(request.form['username'])
    return render_template('test.html')
@app.route('/u' )
def user():
    return render_template('user.html')

@app.route('/p' )
def profile():
    return render_template('profile.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
