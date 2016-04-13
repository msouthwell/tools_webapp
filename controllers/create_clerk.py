from bottle import route, view, template, request, response, redirect
import pymysql.cursors
import pymysql.err
import os
import json
from database import dbapi


@route('/create_clerk', method=['GET'])
@view('create_clerk')
def view_create_clerk():
    return {'message':''}

@route('/create_clerk', method=['POST'])
@view('create_clerk')
def create_clerk():
    login = request.forms.get('login', '').strip()
    first_name = request.forms.get('first_name', '').strip()
    last_name = request.forms.get('last_name', '').strip()
    password = request.forms.get('password', '').strip()

    try:
        connection = dbapi.connect()  # return db connection
        if connection == -1:
            return template('error.tpl', message='Database connection issue.')

        c = connection.cursor()

        sql = "INSERT INTO clerks(login, first_name, last_name, password) VALUES (%s, %s, %s, %s)"

        c.execute(sql,(login, first_name, last_name, password))
        cust_id = c.lastrowid
        connection.commit()

    except pymysql.err.IntegrityError:
        return template('create_clerk.tpl', message="The clerk profile already exists.")
    except pymysql.err.Error as e:
        return template('error.tpl', message='An error occurred. Error {!r}, errno is {}'.format(e, e.args[0]))
    else:
        c.close()
        #return template('view_profile.tpl', message='New customer profile created.', cust_id=cust_id)
        redirect("/view_clerk/%s" % cust_id)
