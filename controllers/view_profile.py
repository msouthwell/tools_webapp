from bottle import route, view, template, request
import pymysql.cursors
from database import dbapi


@route('/view_profile')
@view('view_profile')
def view_session_profile():
    customer_id = int(request.get_cookie('customer_id'))
    print("Found a customer: " + str(customer_id))
    return view_profile(customer_id)


@route('/view_profile/<customer_id>')
@view('view_profile')
def view_profile(customer_id):
    connection = dbapi.connect()  # return db connection
    if connection == -1:
        return template('login.tpl')

    c = connection.cursor()

    sql = "SELECT c.*, r.*, t.*, \
          (SELECT CONCAT (first_name, ' ', last_name) FROM clerks WHERE clerk_id = r.clerk_id_dropoff) AS d_name, \
          (SELECT CONCAT(first_name, ' ', last_name) FROM clerks WHERE clerk_id = r.clerk_id_pickup) AS p_name \
          FROM customers c \
          JOIN reservations r ON (c.customer_id = r.customer_id) \
          JOIN reservations_tools rt ON (r.reservation_id = rt.reservation_id) \
          JOIN tools t ON t.tool_id = (rt.tool_id = t.tool_id) \
          WHERE c.customer_id = %s"

    c.execute(sql, customer_id)
    data = c.fetchone()
    print(data)
    c.close()

    data['message'] = ''  # Template expects a message.  Used for debugging or informing the user of something without altering the template
    return data
