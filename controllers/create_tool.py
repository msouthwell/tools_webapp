from bottle import route, view, template, request, response, redirect
import pymysql.cursors
import pymysql.err
import os
import json
from database import dbapi


@route('/create_tool', method=['GET'])
@view('create_tool')
def view_create_tool():
    try:
        categories = dbapi.get_categories()
        print("categories: " + str(categories))
    except pymysql.err.Error as e:
        return template('error.tpl', message='An error occurred. Error {!r}, errno is {}'.format(e, e.args[0]))

    return {'categories':categories,'message':''}

@route('/create_tool', method=['POST'])
@view('create_tool')
def create_tool():
    short_description = request.forms.get('short_description', '').strip()
    full_description = request.forms.get('full_description', '').strip()
    deposit = request.forms.get('deposit', '').strip()
    day_price = request.forms.get('day_price', '').strip()
    original_price = request.forms.get('original_price', '').strip()
    category_id = request.forms.get('category_id', '').strip()

    try:
        connection = dbapi.connect()  # return db connection
        if connection == -1:
            return template('error.tpl', message='Database connection issue.')

        c = connection.cursor()

        sql = "INSERT INTO tools(short_description, full_description, deposit, day_price, original_price, category_id) VALUES (%s, %s, %s, %s, %s, %s)"

        c.execute(sql,(short_description, full_description, deposit, day_price, original_price, category_id))
        tool_id = c.lastrowid
        connection.commit()

    except pymysql.err.IntegrityError:
        return template('create_tool.tpl', message="The tool already exists.")
    except pymysql.err.Error as e:
        return template('error.tpl', message='An error occurred. Error {!r}, errno is {}'.format(e, e.args[0]))
    else:
        c.close()
        #return template('view_profile.tpl', message='New customer profile created.', cust_id=cust_id)
        redirect("/view_tool/%s" % tool_id)
