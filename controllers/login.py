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

    connection = dbapi.connect()  # return db connection
    if connection == -1:
        return template('error.tpl', message='Database connection issue.')

    if user_type == "clerks":
        sql = "SELECT clerk_id, login, password FROM clerks WHERE login=%s"
    elif user_type == "customers":
        sql = "SELECT customer_id, email, password FROM customers WHERE email=%s"

    print(sql)
    c = connection.cursor()
    c.execute(sql, login)  # login or email
    result = c.fetchone()

    if result is None:
        return template('login.tpl', message='Email or password incorrect')

    c.close()

    if password == result['password']:
        if user_type == "clerks":
            response.set_cookie("clerk_id", str(result['clerk_id']))
            redirect('/clerk_main_menu')
        elif user_type == "customers":
            response.set_cookie("customer_id", str(result['customer_id']))
            redirect('/customer_main_menu')
    else:
        return template('login.tpl', message='Email or password incorrect')
