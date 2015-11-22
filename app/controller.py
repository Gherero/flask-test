__author__ = 'gherero'
from flask import render_template,redirect,url_for
from app import app
from flask import request
from flask import make_response
from app import authentication_functions


@app.route('/')
def index():
    session_id = request.cookies.get('session_id')
    if session_id == None:
        return redirect('login')
    else:
        return redirect('profile')




@app.route('/login', methods=['GET','POST'])
def login():
    session_id = request.cookies.get('session_id')
    if not session_id==None:
        username=authentication_functions.get_username(session_id)
    else:
        if request.method == 'POST':
            login=request.form['login']
            passwd=request.form['password']

            resp = make_response(render_template(...))
            resp.set_cookie('session_id', 'test')

    return render_template('login.html')

@app.route('/y', methods=['GET', 'POST'])
def login_test():
    if request.method == 'POST':
        request.form['username']
    return render_template('test.html')

@app.route('/user' )
def user():
    registration_status = 1
    return render_template('user.html',reg=registration_status)

@app.route('/profile' )
def profile():
    return render_template('profile.html')

@app.route('/logout')
def logout():
    return redirect(url_for('login'))


@app.route('/staff')
def staff():
    return render_template('staff.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

