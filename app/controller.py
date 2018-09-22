__author__ = 'gherero'
from flask import render_template,redirect,url_for
from app import *
from flask import request
from flask import make_response
from app import authentication_functions
from app import queries
from app import time_count
#from app import post_gres_db
from datetime import datetime
from datetime import date
import mysql.connector




def connect_db():
    cnx = mysql.connector.connect(user='test', password='test',
                                  host='127.0.0.1',
                                  database='journal')

    # cursor=cnx.cursor(buffered=True)
    cursor = cnx.cursor(buffered=False)
    return cnx, cursor

def disconnect_db(cnx,cursor):
    cnx.commit()
    cursor.close()
    cnx.close()



"""
@app.after_request
def disconect_db():
    cnx.commit()
    cursor.close()
    cnx.close()
"""

@app.route('/')
def начало():
    return redirect('index')




@app.route('/index')
def index():
    username = authentication_functions.valid_session()
    print("index", username)
    if username == None:
        return redirect('/login')
    else:
        return redirect('/user')




@app.route('/login', methods=['GET','POST'])
def login():
    auth_err=0
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
            print ("/login",login)
            session_id = authentication_functions.magic_id(login)
            authentication_functions.set_session(login,session_id)
            response.set_cookie('session_id',session_id)
            return response
        else:
            auth_err = 1


    return render_template('login.html',err=auth_err)



@app.route('/user',methods=['GET', 'POST'] )
def user():
#    global name, name
    cnx, cursor = connect_db()

    username = authentication_functions.valid_session()
    if username == None:
        return redirect('login')

    #registration_status = 0

    cursor.execute(queries.query_user % (username.decode()))
    (name, surname, work_from, pozition,phone, mail, access_level) = cursor.fetchone()

    cursor.execute(queries.get_registration_status % (username.decode()))
    registration_status, = cursor.fetchone()

    cursor.execute(queries.get_last_registration % (username.decode()))
    last_registration_time, = cursor.fetchone()
    print(last_registration_time.date())

    cursor.execute(queries.get_time_reg_today % date.today())
    time_reg_today = cursor.fetchall()
    hourse_on_work_today = time_count.count(time_reg_today)
    print(time_reg_today)
    print(type(time_reg_today))
    print(len(time_reg_today))

    if request.method == 'POST':
        s_reg = int(request.form['regbutton'])
        if s_reg == 1 :
            registration_status=1
        else:
            registration_status=0
        set_reg = (username.decode(), datetime.now(), registration_status)
        cursor.execute(queries.time_tracking,set_reg)

    disconnect_db(cnx,cursor)

    return render_template('user.html',
                           name_surname = name+" "+surname,
                           login = username.decode(),
                           reg = registration_status,
                           working_with = work_from,
                           last_registration = last_registration_time.date(),
                           post = pozition,
                           phone = phone,
                           mail = mail,
                           access_level = access_level,
                           reg_button_name = "Зарегистрироваться",
                           unred_button_name = "Телепортироваться домой"
                           )





@app.route('/get_cookie')
def get_cookie():
    s=request.cookies.get('session_id')
#    print(s)
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

