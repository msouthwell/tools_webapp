from bottle import route, view, request, response
from datetime import datetime
import pymysql.cursors

connection = pymysql.connect(host='localhost',
                             db='test',
                             user='root',
                             charset='utf8',
                             cursorclass=pymysql.cursors.DictCursor)

cursor = connection.cursor()


@route('/about')
@view('about')
def about():
    """Renders the about page."""
    sql = "SELECT * FROM clerks"
    cursor.execute(sql)
    row = cursor.fetchone()
    connection.close()
    return dict(
        title='About',
        message=row,
        year=datetime.now().year)
