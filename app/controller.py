__author__ = 'gherero'
from flask import render_template,redirect,url_for
from app import *
from flask import request
from flask import make_response
from app import authentication_functions
from app import queries
#from app import post_gres_db
import mysql.connector

cnx = mysql.connector.connect(user='test', password='test',
                              host='127.0.0.1',
                              database='journal')
cursor=cnx.cursor(buffered=True)


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


    return render_template('login.html',err=auth_err)



@app.route('/user',methods=['GET', 'POST'] )
def user():
    global name, name
    username = authentication_functions.valid_session()
    if username == None:
        return redirect('login')

    registration_status = 0

    cursor.execute(queries.query_user % (username.decode()))

    (name, surname, work_from, pozition,phone, mail, access_level) = cursor.fetchone()

    #print(cursor.fetchall(),"cur_fetchall")

#    for (name, surname, work_from, pozition,phone, mail, access_level) in cursor:
#        print("{}, {}, {}, {}, {}, {}, {}".format(name, surname, work_from, pozition,phone, mail, access_level))

    print(name)

    if request.method == 'POST':
        s_reg = int(request.form['regbutton'])

        if s_reg == 1 :
            registration_status=1
        else:
            registration_status=0
        print(type(s_reg))
    #    jour_db=post_gres_db.Time_registarion.create(user_id='550e8400-e29b-41d4-a716-446655440000',username=username,registration_status=s_reg,created_date=datetime.now())
    print(work_from)

    return render_template('user.html',
                           name_surname=name+" "+surname,
                           login=username.decode(),
                           reg=registration_status,
                           working_with= work_from,
                           last_registration= '2.5.2014',
                           post=pozition,
                           phone=phone,
                           mail=mail,
                           access_level=access_level,
                           reg_button_name= "Зпрегистрироваться",
                           unred_button_name="Телепортироваться домой"
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

