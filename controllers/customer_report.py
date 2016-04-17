from bottle import route, view, template, request, response
import pymysql.cursors
import pymysql.err
import datetime
import calendar
from database import dbapi

@route('/customer_report')
@view('customer_report')
def generate_customer_report():
    try:
        connection = dbapi.connect()
        c = connection.cursor()

        sql = "SELECT C.email, C.last_name, C.first_name, COUNT(RT.tool_id)AS rentals\
               FROM \
               CUSTOMERS AS C JOIN \
               RESERVATIONS AS R ON C.customer_id=R.customer_id JOIN \
               RESERVATIONS_TOOLS AS RT ON R.reservation_id=RT.reservation_id \
               WHERE \
               R.start_date<=%s AND R.end_date>=%s \
               GROUP BY C.email \
               ORDER BY rentals DESC, C.last_name"

        now = datetime.datetime.now()
        start_of_month = '%d-%d-%d' % (now.year, now.month, 1)
        last_day = calendar.monthrange(now.year, now.month)
        end_of_month = '%d-%d-%d' % (now.year, now.month, last_day[1])

        c.execute(sql, ( end_of_month, start_of_month))

        rows = c.fetchall()
    except pymysql.err.Error as e:
        return template('error.tpl', message='An error occurred. Error {!r}, errno is {}'.format(e, e.args[0]))
    finally:
        c.close()

    return template('customer_report', rows=rows)
