from bottle import route, view, template, request, response
import pymysql.cursors
import pymysql.err
import datetime, time
from database import dbapi

@route('/sell', method=['POST'])
@view('sell')
def sell_the_tool():
    c = None

    tool_id = int(request.forms.get('tool_id', ''))
    clerk_id = int(request.get_cookie('clerk_id'))
    sale_date = time.strftime('%Y-%m-%d %H:%M:%S') 

    try:
        connection = dbapi.connect()
        c = connection.cursor()
        sql = "INSERT INTO sells(tool_id, clerk_id, sale_date) VALUES (%s, %s, %s)"
        c.execute(sql, (tool_id, clerk_id, sale_date))
        connection.commit()

    except pymysql.err.Error as e:
        return template('error.tpl', message='An error occurred. Error {!r}, errno is {}'.format(e, e.args[0]))

    finally:
        if c is not None:
            c.close()

    return
    
@route('/sell_tool', method=['GET'])
@view('sell')
def sell_tool_get():
    return {'tool_id':''}

@route('/sell_tool', method=['POST'])
@view('sell_tool')
def sell_tool_post():
    tool_id = int(request.forms.get('tool_id', ''))

    try:
        connection = dbapi.connect()  # return db connection

        c = connection.cursor()

        c.execute("SELECT *, (original_price / 2) AS sell_price FROM tools AS t JOIN categories AS c ON t.category_id = c.category_id WHERE t.tool_id = %s", (tool_id))
        data = c.fetchone()
        c.close()
    except pymysql.err.Error as e:
        return template('error.tpl', message='An error occurred. Error {!r}, errno is {}'.format(e, e.args[0]))

    return data
