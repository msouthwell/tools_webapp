from bottle import route, view, template, request, response
import pymysql.cursors
import pymysql.err
import os
import json
from database import dbapi


@route('/view_profile')
@view('view_profile')
def view_session_profile():
    customer_id = int(request.get_cookie('customer_id'))
    print("Found a customer: " + str(customer_id))
    return view_profile(customer_id)

@route('/view_profile/<customer_id>')
@view('view_profile')
def view_profile(customer_id):
    try:
        connection = dbapi.connect()  # return db connection

        c = connection.cursor()

        sql = "SELECT * FROM customers WHERE customer_id = %s"

        c.execute(sql, customer_id)
        data = c.fetchone()
        c.close()
    except pymysql.err.Error as e:
        return template('error.tpl', message='An error occurred. Error {!r}, errno is {}'.format(e, e.args[0]))
    else:
        data['message'] = ''  # Template expects a message.  Used for debugging or informing the user of something without altering the template
        return data
