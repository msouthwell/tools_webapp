from bottle import route, view, template, request, response
import pymysql.cursors
import pymysql.err
from database import dbapi


@route('/view_tool', method=['POST'])
@view('view_tool')
def view_tool_post():
    tool_id = request.forms.get('tool_id', '').strip()
    return view_tool(tool_id)
    
@route('/view_tool/<tool_id>')
@view('view_tool')
def view_tool(tool_id):
    try:
        connection = dbapi.connect()  # return db connection
        if connection == -1:
            return template('error.tpl', message='Database connection issue.')

        c = connection.cursor()

        c.execute("SELECT * FROM tools AS t JOIN categories AS c ON t.category_id = c.category_id WHERE t.tool_id = %s", (tool_id))
        data = c.fetchone()
        c.close()
    except pymysql.err.Error as e:
        return template('error.tpl', message='An error occurred. Error {!r}, errno is {}'.format(e, e.args[0]))

    return data