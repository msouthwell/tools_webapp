from bottle import route, view, template, request, response, redirect
import pymysql.cursors
import pymysql.err
import os
import json
from database import dbapi


@route('/login', method=['GET'])
@view('login')
def view_login():
    return {'message':''}

@route('/login', method=['POST'])
@view('login')
def login():
    login = request.forms.get('login', '').strip()
    password = request.forms.get('password', '').strip()
    user_type = request.forms.get('usertype', '').strip()
    
    c = None

    try:
        connection = dbapi.connect()  # return db connection

        c = connection.cursor()

        if user_type == "clerks":
            sql = "SELECT clerk_id, login, password FROM clerks WHERE login=%s"
            c.execute(sql, (login))  # login or email
            result = c.fetchone()
            
            if result is not None and password == result['password']:
                response.set_cookie("clerk_id", str(result['clerk_id']))
                redirect('/clerk_main_menu')
            else:
                return {'message':'Login or password incorrect'}

        elif user_type == "customers":
            sql = "SELECT customer_id, email, password FROM customers WHERE email=%s"
            c.execute(sql, (login))  # login or email
            result = c.fetchone()

            if result is not None:
                if password == result['password']:
                    response.set_cookie("customer_id", str(result['customer_id']))
                    redirect('/customer_main_menu')
                else:
                    return {'message':'Email or password incorrect'}
            else:
                redirect('/create_profile')

    except pymysql.err.Error as e:
        return template('error.tpl', message='An error occurred. Error {!r}, errno is {}'.format(e, e.args[0]))
    finally:
        if c is not None:
            c.close()
