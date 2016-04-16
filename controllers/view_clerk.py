from bottle import route, view, template, request, response
import pymysql.cursors
import pymysql.err
import os
import json
from database import dbapi


@route('/view_clerk')
@view('view_clerk')
def view_session_clerk():
    clerk_id = int(request.get_cookie('clerk_id'))
    print("Found a clerk: " + str(clerk_id))
    return view_clerk(clerk_id)

@route('/view_clerk/<clerk_id>')
@view('view_clerk')
def view_clerk(clerk_id):
    try:
        connection = dbapi.connect()  # return db connection

        c = connection.cursor()

        sql = "SELECT * FROM clerks WHERE clerk_id = %s"

        c.execute(sql, (clerk_id))
        data = c.fetchone()
    except pymysql.err.Error as e:
        return template('error.tpl', message='An error occurred. Error {!r}, errno is {}'.format(e, e.args[0]))
    else:
        data['message'] = ''  # Template expects a message.  Used for debugging or informing the user of something without altering the template
        return data
    finally:
        c.close()

