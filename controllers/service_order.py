from bottle import route, view, template, request, response, redirect
import pymysql.err
import datetime
from database import dbapi


@route('/service_order', method=['GET'])
@view('service_order')
def view_service_order():
    return {'tool_id':'', 'start_date':'', 'end_date':'', 'cost':'', 'message':''}

@route('/service_order', method=['POST'])
@view('service_order')
def process_service_order():
    tool_id = int(request.forms.get('tool_id', ''))
    start_date = request.forms.get('start_date', '')
    start_date_datetime = datetime.datetime.strptime(start_date, '%m/%d/%Y')
    print("start: {:%b, %d %Y}".format(start_date_datetime))
    end_date = request.forms.get('end_date', '')
    end_date_datetime = datetime.datetime.strptime(end_date, '%m/%d/%Y')
    print("end: {:%b, %d %Y}".format(end_date_datetime))
    cost = float(request.forms.get('cost', ''))

    try:
        reserved_tools = [{'tool_id':tool_id}]
        no_longer_availables = dbapi.check_available_tools(reserved_tools, start_date_datetime, end_date_datetime)
        print('not_available_for_service' + str(no_longer_availables))
        if len(no_longer_availables) > 0:
            return {'tool_id':tool_id, 'start_date':start_date, 'end_date':end_date, 'cost':cost, 'message':'Tool ' + str(tool_id) + ' is not available for service.'}

        clerk_id = int(request.get_cookie('clerk_id'))

        connection = dbapi.connect()  # return db connection

        c = connection.cursor()

        c.execute("INSERT INTO service_orders(clerk_id, tool_id, start_date, end_date, est_cost) VALUES(%s, %s, %s, %s, %s)", (clerk_id, tool_id, start_date_datetime, end_date_datetime, cost))

        connection.commit()
    except pymysql.err.Error as e:
        return template('error.tpl', message='An error occurred. Error {!r}, errno is {}'.format(e, e.args[0]))

    return {'tool_id':'', 'start_date':'', 'end_date':'', 'cost':'', 'message':'Service order added.'}
