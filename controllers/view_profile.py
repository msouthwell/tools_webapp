from bottle import route, view, template, request
import pymysql.cursors
import copy
from database import dbapi
from controllers import utilities


@route('/view_profile')
@view('view_profile')
def view_session_profile():
    customer_id = int(request.get_cookie('customer_id'))
    print("Found a customer: " + str(customer_id))
    return view_profile(customer_id)


@route('/view_profile/<customer_id>')
@view('view_profile')
def view_profile(customer_id):
    print(customer_id)

    try:
        connection = dbapi.connect()  # return db connection

        c = connection.cursor()

        c.execute("SELECT CONCAT(first_name, ' ', last_name) AS customer_name, email, address, \
                CONCAT(work_phone_cc, ' ', work_phone_number) AS work_phone, CONCAT(home_phone_cc, ' ', home_phone_number) AS home_phone \
                FROM customers \
                WHERE customer_id = %s", (customer_id))
        customer = c.fetchone()

    except pymysql.err.Error as e:
        return template('error.tpl', message='An error occurred. Error {!r}, errno is {}'.format(e, e.args[0]))
    finally:
        c.close()

    reservations = utilities.get_reservation_details_by_customer(customer_id)

    return {'customer':customer, 'reservations':reservations, 'message':''}
