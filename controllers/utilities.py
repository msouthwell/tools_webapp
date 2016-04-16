
from bottle import template
import pymysql.cursors
import pymysql.err
from database import dbapi

# returns the reservation data
def view_reservation(reservation_id):

    try:
        connection = dbapi.connect()
        if connection == -1:
            return template('error.tpl', message="Database could not connect");

        c = connection.cursor()

        sql = "SELECT * FROM RESERVATIONS " \
            "WHERE reservation_id = %s"
        c.execute(sql, reservation_id)
        data= c.fetchone()
        c.close()
    except pymysql.err.Error as e:
        return template('error.tpl', message='An error occurred. Error {!r}, errno is {}'.format(e, e.args[0]))
    else:
        return data

# there is likely a way simpler and more elegant way to do this, but it works for now
def date_differance(start_date, end_date):
    try:
        connection = dbapi.connect()
        if connection == -1:
            return template('error.tpl', message="Database could not connect");

        c = connection.cursor()
        dd = "SELECT DATEDIFF (%s, %s) AS Diffdate"
        c.execute(dd, (str(end_date), str(start_date)))
        datediff = c.fetchone()
        c.close()
    except pymysql.err.Error as e:
        return template('error.tpl', message='An error occurred. Error {!r}, errno is {}'.format(e, e.args[0]))
    else:
        return datediff['Diffdate']

def reservation_tools(reservation_id):

    try:
        connection = dbapi.connect()
        if connection == -1:
            return template('error.tpl', message="Database could not connect");

        c = connection.cursor()

        sql = "SELECT * FROM RESERVATIONS_TOOLS NATURAL JOIN TOOLS " \
            "WHERE reservation_id = %s"
        c.execute(sql, reservation_id)
        data= c.fetchall()
        c.close()
    except pymysql.err.Error as e:
        return template('error.tpl', message='An error occurred. Error {!r}, errno is {}'.format(e, e.args[0]))
    else:
        return data

def update_credit_card(reservation_id, cc, ed):

    try:
        connection = dbapi.connect()
        if connection == -1:
            return template('error.tpl', message="Database could not connect");

        c = connection.cursor()

        sql = "UPDATE RESERVATIONS SET credit_card=%s,expiration_date=%s WHERE reservation_id = %s"

        c.execute(sql, (cc, ed, reservation_id))
        c.close()
    except pymysql.err.Error as e:
        return template('error.tpl', message='An error occurred. Error {!r}, errno is {}'.format(e, e.args[0]))
