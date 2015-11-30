__author__ = 'gherero'
from flask import render_template,redirect,url_for
from app import app
from flask import request
from flask import make_response
from app import authentication_functions




@app.route('/')
def начало():
    return redirect('index')




@app.route('/index')
def index():
    username = authentication_functions.valid_session()
    if username == None:
        return redirect('/login')
    else:
        return redirect('/user')




@app.route('/login', methods=['GET','POST'])
def login():
    auth_err=1
    username = authentication_functions.valid_session()
    if not username == None:
        return redirect('user')

    if request.method == 'POST':
        login=request.form['login']
        passwd=request.form['password']
        print(login,passwd)
        if login=='test' and passwd == 'test':

            redirect_to_index = redirect('/index')
            response = app.make_response(redirect_to_index )
            session_id = authentication_functions.magic_id(login)
            response.set_cookie('session_id',session_id)
            authentication_functions.set_session(login,session_id)
            return response

    return render_template('login.html',err=auth_err)



@app.route('/user',methods=['GET', 'POST'] )
def user():
    registration_status = 0
    if request.method == 'POST':
        registration_status = 1
        print(request.form['regbutton'])


    return render_template('user.html',
                           login='Holmes',
                           reg=registration_status,
                           middle_name='test',
                           working_with= '2.3.2004',
                           last_registration= '2.5.2014',
                           post='boss',
                           phone=322223554,
                           mail='boss@baoos.ua',
                           access_level='пользователь'
                           )





@app.route('/get_cookie')
def get_cookie():
    s=request.cookies.get('session_id')
    print(s)
    return s



@app.route('/set_cookie')
def cookie_insertion():
    redirect_to_index = redirect('/index')
    response = app.make_response(redirect_to_index )
    s=authentication_functions.magic_id("test")
    response.set_cookie('session_id',s)
    return response











@app.route('/y', methods=['GET', 'POST'])
def login_test():
    if request.method == 'POST':
        request.form['username']
    return render_template('test.html')


@app.route('/profile' )
def profile():
    username = authentication_functions.valid_session()
    if username == None:
        return redirect('/login')
    return render_template('profile.html')



@app.route('/logout')
def logout():
    authentication_functions.del_session()
    return redirect(url_for('login'))


@app.route('/staff')
def staff():
    return render_template('staff.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

