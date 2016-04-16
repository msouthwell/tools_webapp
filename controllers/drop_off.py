from bottle import route, view, template, request, response
from controllers import utilities
import pymysql.cursors
import pymysql.err
from database import dbapi
import sys
import datetime

@route('/drop_off', method=['GET'])
@view('drop_off_select')
def reservation_select():
    if request.GET.get('Submit', '').strip():
        id = request.GET.get('id', '').strip()
        return drop_off(id)
    else:
        return {'message': ''}

@route('/drop_off/<reservation_id>', method=['POST'])
def drop_off(reservation_id):

    try:
        utilities.update_dropoff_clerk(reservation_id)
        data = utilities.view_reservation(reservation_id)

        tools = utilities.reservation_tools(reservation_id)

        connection = dbapi.connect()  # return db connection
        c = connection.cursor()
        sql = "SELECT first_name, last_name FROM customers WHERE customer_id = %s"
        c.execute(sql, data['customer_id'])
        tmp = c.fetchone()
        data['customer_name'] = tmp['first_name'] + ' ' + tmp['last_name']
        sql = "SELECT first_name, last_name FROM clerks WHERE clerk_id = %s"
        c.execute(sql, data['clerk_id_dropoff'])
        tmp = c.fetchone()
        data['clerk_dropoff_name'] = tmp['first_name'] + ' ' + tmp['last_name']
        c.close()

        deposit = 0
        rental = 0

        for row in tools:
            deposit += row['deposit']
            rental += row['day_price']

        data['rental_cost'] = rental * utilities.date_differance(data['start_date'], data['end_date'])
        data['deposit_held'] = deposit
        data['remaining_cost'] = data['rental_cost'] - data['deposit_held']
    except pymysql.err.Error as e:
        return template('error.tpl', message='An error occurred. Error {!r}, errno is {}'.format(e, e.args[0]))
    except:
        return template('error.tpl', message='An error occurred in drop_off')
    else:
        return template('drop_off.tpl', data)