from bottle import route, view, template, request, response, redirect
import datetime
from database import dbapi


@route('/check_available_tools', method=['GET'])
@view('check_available_tools')
def view_check_avilable_tools():
    # Not sure if this is even needed
    pass

@route('/check_available_tools', method=['POST'])
@view('available_tools')
def check_avilable_tools_post():
    category = request.forms.get('category', '1').strip()
    print("category: " + str(category))
    start_date = datetime.datetime.strptime(request.forms.get('start_date', ''), '%m/%d/%Y')
    print("start: {:%b, %d %Y}".format(start_date))
    end_date = datetime.datetime.strptime(request.forms.get('end_date', ''), '%m/%d/%Y')
    print("end: {:%b, %d %Y}".format(end_date))

    connection = dbapi.connect()  # return db connection
    if connection == -1:
        return template('error.tpl', message='Database connection issue.')

    c = connection.cursor()

    c.execute("SELECT t.tool_id, t.short_description, t.deposit, t.day_price FROM tools AS t WHERE category_id = %s AND NOT EXISTS"+
              "(SELECT * FROM reservations AS r JOIN reservations_tools AS rt ON r.reservation_id = rt.reservation_id WHERE t.tool_id = rt.tool_id AND r.start_date <= %s AND r.end_date >= %s) "+
              "AND NOT EXISTS(SELECT * FROM sells AS s WHERE t.tool_id = s.tool_id)", (category, end_date, start_date))

    rows = c.fetchall()

    for row in rows:
        print("row: " + str(row))

    c.close()

    return {'rows':rows}
