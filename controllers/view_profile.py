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

    # TODO sql needs a lot of work. Need to lookup tool information and clerk inforamtion
    sql = "SELECT * FROM customers x, reservations WHERE x.customer_id = %s"

    c.execute(sql, customer_id)
    data = c.fetchone()
    print(data)
    c.close()

    data['message'] = ''  # Template expects a message.  Used for debugging or informing the user of something without altering the template
    return data
