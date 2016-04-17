from bottle import route, view, template, request
import pymysql.cursors
from database import dbapi
import copy


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
    connection = dbapi.connect()  # return db connection
    if connection == -1:
        return template('login.tpl')

    c = connection.cursor()

    sql = "SELECT c.*,r.*, t.short_description, t.deposit, rt.*, t.day_price, \
            (SELECT CONCAT (first_name, ' ', last_name) FROM clerks WHERE clerk_id = r.clerk_id_dropoff) AS d_name, \
            (SELECT CONCAT(first_name, ' ', last_name) FROM clerks WHERE clerk_id = r.clerk_id_pickup) AS p_name \
            FROM customers c \
            JOIN reservations r ON (c.customer_id = r.customer_id) \
            LEFT JOIN reservations_tools rt ON (r.reservation_id = rt.reservation_id) \
            LEFT OUTER JOIN tools t ON (t.tool_id = rt.tool_id) \
            WHERE c.customer_id = %s \
            ORDER BY r.start_date"

    c.execute(sql, customer_id)
    data = c.fetchall()

    print(type(data))
    print('-------------------')

    # just get customer information, no reservations for customer
    if not data:
        sql = "SELECT * FROM customers WHERE customer_id = %s"
        c.execute(sql, customer_id)
        data = c.fetchall()
        output = template('view_profile', rows=data)
        c.close()
        return output
    else:
        # Giving up on doing this in pure sql
        formatted_data = []
        formatted_ids = []

        for row in data:
            res_id = row['reservation_id']
            new_dict = copy.deepcopy(row)
            if res_id in formatted_ids:
                continue
            for row2 in data:
                if row['reservation_id'] == row2['reservation_id'] and \
                        row['tool_id'] != row2['tool_id'] and \
                        row['reservation_id'] not in formatted_ids:

                    new_dict['day_price'] = new_dict['day_price'] + row2['day_price']
                    new_dict['deposit'] = new_dict['deposit'] + row2['deposit']

                    new_dict['short_description'] = new_dict['short_description'] + \
                        ', ' + row2['short_description']

            formatted_data.append(new_dict)
            formatted_ids.append(res_id)

        print(formatted_data)
        output = template('view_profile', rows=formatted_data)

        c.close()
        return output
