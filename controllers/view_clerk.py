from bottle import route, view, template, request, response
import pymysql.cursors
import pymysql.err
import os
import json
from database import dbapi


@route('/view_clerk/<clerk_id>')
@view('view_clerk')
def view_clerk(clerk_id):
    try:
        connection = dbapi.connect()  # return db connection
        if connection == -1:
            return template('error.tpl', message='Database connection issue.')

        c = connection.cursor()

        sql = "SELECT * FROM clerks WHERE clerk_id = %s"

        c.execute(sql, clerk_id)
        data = c.fetchone()
        c.close()
    except pymysql.err.Error as e:
        return template('error.tpl', message='An error occurred. Error {!r}, errno is {}'.format(e, e.args[0]))
    else:
        data['message']=''  # Template expects a message.  Used for debugging or informing the user of something without altering the template
        return data
