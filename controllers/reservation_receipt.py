from bottle import route, view, template, request, response
from controllers import utilities
import pymysql.cursors
import pymysql.err
from database import dbapi
import sys
import datetime

@route('/reservation_receipt/<reservation_id>', method=['POST'])
def reservation_receipt(reservation_id):

    try:
        credit_card = request.forms.get('credit_card', '').strip()
        expiration_date = request.forms.get('expiration_date', '')
        expiration_date_datetime = datetime.datetime.strptime(expiration_date, '%m/%d/%Y')
        utilities.update_credit_card(reservation_id, credit_card, expiration_date_datetime)

        utilities.update_pickup_clerk(reservation_id)

        reservation = utilities.view_reservation(reservation_id)
        tools = utilities.reservation_tools(reservation_id)
        data = reservation.copy()

        connection = dbapi.connect()  # return db connection

        c = connection.cursor()
        sql = "SELECT first_name, last_name FROM customers WHERE customer_id = %s"
        c.execute(sql, data['customer_id'])
        tmp = c.fetchone()
        data['customer_name'] = tmp['first_name'] + ' ' + tmp['last_name']
        sql = "SELECT first_name, last_name FROM clerks WHERE clerk_id = %s"
        c.execute(sql, data['clerk_id_pickup'])
        tmp = c.fetchone()
        data['clerk_pickup_name'] = tmp['first_name'] + ' ' + tmp['last_name']
        c.close()

        table = ""
        deposit = 0
        rental = 0

        for row in tools:
            table = table + "<tr><td>{tool_id}</td><td>{short_description}</td></tr>".format(tool_id=row['tool_id'], short_description=row['short_description'])
            deposit += row['deposit']
            rental += row['day_price']

        data['tool_table'] = table
        data['deposit_required'] = deposit
        rental = rental * utilities.date_differance(reservation['start_date'], reservation['end_date'])
        data['estimated_cost'] = rental
        data['credit_card'] = credit_card
        data['expiration_date'] = expiration_date

    except pymysql.err.Error as e:
        return template('error.tpl', message='An error occurred. Error {!r}, errno is {}'.format(e, e.args[0]))
    except:
        return template('error.tpl', message='An error occurred in pick_up_reservation')
    else:
        return template('reservation_receipt.tpl', data)
