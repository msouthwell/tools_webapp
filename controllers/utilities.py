
from bottle import template, request
import pymysql.cursors
import pymysql.err
from database import dbapi

# returns the reservation data
def view_reservation(reservation_id):
    try:
        connection = dbapi.connect()

        c = connection.cursor()

        sql = "SELECT * FROM RESERVATIONS " \
            "WHERE reservation_id = %s"
        c.execute(sql, (reservation_id))
        data = c.fetchone()
    except pymysql.err.Error as e:
        return template('error.tpl', message='An error occurred. Error {!r}, errno is {}'.format(e, e.args[0]))
    else:
        return data
    finally:
        c.close()

def date_differance(start_date_datetime, end_date_datetime):
    delta = end_date_datetime - start_date_datetime
    return delta.days

def tool_accessories(tool_id):
    c = None

    try:
        connection = dbapi.connect()
        c = connection.cursor()
        sql = "SELECT * FROM tool_accessories NATURAL JOIN tools WHERE tool_id  = %s"
        c.execute(sql, (tool_id))
        data = c.fetchall()

    except pymysql.err.Error as e:
        return

    else:
        return data

    finally:
        if c is not None:
            c.close()

def reservation_tools(reservation_id):
    try:
        connection = dbapi.connect()

        c = connection.cursor()

        sql = "SELECT * FROM RESERVATIONS_TOOLS NATURAL JOIN TOOLS " \
            "WHERE reservation_id = %s"
        c.execute(sql, (reservation_id))
        data = c.fetchall()
    except pymysql.err.Error as e:
        return template('error.tpl', message='An error occurred. Error {!r}, errno is {}'.format(e, e.args[0]))
    else:
        return data
    finally:
        c.close()

def update_pickup_clerk(reservation_id):
    try:
        connection = dbapi.connect()

        c = connection.cursor()

        sql = "UPDATE RESERVATIONS SET clerk_id_pickup=%s WHERE reservation_id = %s"
        clerk_id = int(request.get_cookie('clerk_id'))
        c.execute(sql, (clerk_id, reservation_id))
        connection.commit()
    except pymysql.err.Error as e:
        return template('error.tpl', message='An error occurred. Error {!r}, errno is {}'.format(e, e.args[0]))
    finally:
        c.close()

def update_dropoff_clerk(reservation_id):
    try:
        connection = dbapi.connect()

        c = connection.cursor()

        sql = "UPDATE RESERVATIONS SET clerk_id_dropoff=%s WHERE reservation_id = %s"
        clerk_id = int(request.get_cookie('clerk_id'))
        c.execute(sql, (clerk_id, reservation_id))
        connection.commit()
    except pymysql.err.Error as e:
        return template('error.tpl', message='An error occurred. Error {!r}, errno is {}'.format(e, e.args[0]))
    finally:
        c.close()

def update_credit_card(reservation_id, cc, ed):
    try:
        connection = dbapi.connect()

        c = connection.cursor()

        sql = "UPDATE RESERVATIONS SET credit_card=%s,expiration_date=%s WHERE reservation_id = %s"

        c.execute(sql, (cc, ed, reservation_id))
        connection.commit()
    except pymysql.err.Error as e:
        return template('error.tpl', message='An error occurred. Error {!r}, errno is {}'.format(e, e.args[0]))
    finally:
        c.close()

def get_reservation_details(reservation_id):
    try:
        connection = dbapi.connect()

        c = connection.cursor()

        c.execute("SELECT  r.reservation_id, r.start_date, r.end_date, r.credit_card, r.expiration_date, c.customer_id, \
                CONCAT(c.first_name, ' ', c.last_name) AS customer_name, \
                CONCAT(d.first_name, ' ', d.last_name) dropoff_clerk, \
                CONCAT(p.first_name, ' ', p.last_name) pickup_clerk, \
                t.tool_id, short_description, deposit, day_price \
                FROM \
                    customers c \
                        JOIN \
                    reservations r ON (c.customer_id = r.customer_id) \
                        JOIN \
                    reservations_tools rt ON (r.reservation_id = rt.reservation_id) \
                        LEFT OUTER JOIN \
                    tools t ON (t.tool_id = rt.tool_id) \
                        LEFT OUTER JOIN \
                    clerks d ON (r.clerk_id_dropoff = d.clerk_id) \
                        LEFT OUTER JOIN \
                    clerks p ON (r.clerk_id_pickup = p.clerk_id) \
                WHERE \
                    r.reservation_id = %s \
                ORDER BY r.start_date , r.reservation_id", (reservation_id))
        rows = c.fetchall()
    except pymysql.err.Error as e:
        return template('error.tpl', message='An error occurred. Error {!r}, errno is {}'.format(e, e.args[0]))
    finally:
        c.close()

    return get_reservation_data(rows)

def get_reservation_details_by_customer(customer_id):
    try:
        connection = dbapi.connect()

        c = connection.cursor()

        c.execute("SELECT  r.reservation_id, r.start_date, r.end_date, r.credit_card, r.expiration_date, c.customer_id, \
                CONCAT(c.first_name, ' ', c.last_name) AS customer_name, \
                CONCAT(d.first_name, ' ', d.last_name) dropoff_clerk, \
                CONCAT(p.first_name, ' ', p.last_name) pickup_clerk, \
                t.tool_id, short_description, deposit, day_price \
                FROM \
                    customers c \
                        JOIN \
                    reservations r ON (c.customer_id = r.customer_id) \
                        JOIN \
                    reservations_tools rt ON (r.reservation_id = rt.reservation_id) \
                        LEFT OUTER JOIN \
                    tools t ON (t.tool_id = rt.tool_id) \
                        LEFT OUTER JOIN \
                    clerks d ON (r.clerk_id_dropoff = d.clerk_id) \
                        LEFT OUTER JOIN \
                    clerks p ON (r.clerk_id_pickup = p.clerk_id) \
                WHERE \
                    c.customer_id = %s \
                ORDER BY r.start_date , r.reservation_id", (customer_id))
        rows = c.fetchall()
    except pymysql.err.Error as e:
        return template('error.tpl', message='An error occurred. Error {!r}, errno is {}'.format(e, e.args[0]))
    finally:
        c.close()

    return get_reservation_data(rows)

# Returns a list reservations for all reservations represented in the rows. This maps a 1:M relationship in SQL
# to a structure
def get_reservation_data(rows):
    reservations = []

    last_reservation_id = -1
    reservation = None
    for row in rows:
        if (row['reservation_id'] != last_reservation_id):
            # bookkeeping for a new reservation; only done once for a new reservation
            reservation = {}
            reservations.append(reservation)
            last_reservation_id = row['reservation_id'];

            # copy reservation information
            reservation['reservation_id'] = row['reservation_id']
            reservation['start_date'] = row['start_date']
            reservation['end_date'] = row['end_date']
            reservation['credit_card'] = row['credit_card']
            reservation['expiration_date'] = row['expiration_date']
            reservation['customer_id'] = row['customer_id']
            reservation['customer_name'] = row['customer_name']
            reservation['dropoff_clerk'] = row['dropoff_clerk']
            reservation['pickup_clerk'] = row['pickup_clerk']

            # initialized calculated data
            reservation['total_deposit'] = 0.0
            reservation['total_rental'] = 0.0
            reservation['days'] = date_differance(reservation['start_date'], reservation['end_date'])
            reservation['tools'] = []

        # each row has a tool, so add the tool to the current list of tools
        tool = {}
        reservation['tools'].append(tool)
        tool['tool_id'] = row['tool_id']
        tool['short_description'] = row['short_description']
        tool['deposit'] = row['deposit']
        tool['day_price'] = row['day_price']

        # update the calculated data
        reservation['total_deposit'] += float(tool['deposit'])
        reservation['total_rental'] += float(tool['day_price']) * reservation['days']

    print("Returning reservations: " + str(reservations))
    return reservations
