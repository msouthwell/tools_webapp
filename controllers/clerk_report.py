from bottle import route, view, template, request, response
import pymysql.cursors
import pymysql.err
from database import dbapi
import datetime
import calendar

@route('/clerk_report')
@view('clerk_report')
def generate_clerk_report():
    try:
        connection = dbapi.connect()
        c = connection.cursor()

        sql = "SELECT CONCAT (C.first_name, ' ', C.last_name) as clerk_name, \
               COALESCE ( P.rcount, 0) AS pickup_count, \
               COALESCE ( D.rcount, 0) AS dropoff_count, \
               COALESCE ( P.rcount, 0) + COALESCE( D.rcount,0) AS total_count \
               FROM \
               CLERKS C LEFT JOIN (SELECT PICKUPS.clerk_id_pickup, COUNT(*) \
               AS rcount FROM RESERVATIONS AS PICKUPS WHERE \
               PICKUPS.clerk_id_pickup IS NOT NULL \
               AND PICKUPS.start_date BETWEEN %s AND %s \
               GROUP BY PICKUPS.clerk_id_pickup) \
               P ON C.clerk_id=P.clerk_id_pickup \
               LEFT JOIN \
               (SELECT DROPOFFS.clerk_id_dropoff, COUNT(*) AS rcount \
               FROM RESERVATIONS AS DROPOFFS \
               WHERE \
               DROPOFFS.clerk_id_dropoff IS NOT NULL \
               AND DROPOFFS.end_date BETWEEN %s AND %s \
               GROUP BY DROPOFFS.clerk_id_dropoff ) \
               D ON C.clerk_id=D.clerk_id_dropoff \
               ORDER BY total_count DESC"

        now = datetime.datetime.now()
        start_of_month = '%d-%d-%d' % (now.year, now.month, 1)
        last_day = calendar.monthrange(now.year, now.month)
        end_of_month = '%d-%d-%d' % (now.year, now.month, last_day[1])

        print(end_of_month)

        c.execute(sql, (start_of_month, end_of_month, start_of_month, end_of_month))

        rows = c.fetchall()
        print(rows)
    except pymysql.err.Error as e:
        return template('error.tpl', message='An error occurred. Error {!r}, errno is {}'.format(e, e.args[0]))
    finally:
        c.close()

    return template('clerk_report', rows=rows)