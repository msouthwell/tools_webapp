from bottle import route, view, template, request, response, redirect
import pymysql.err
import datetime
from database import dbapi


@route('/check_available_tools', method=['GET'])
@view('check_available_tools')
def view_check_avilable_tools():
    try:
        categories = dbapi.get_categories()
        print("categories: " + str(categories))
    except pymysql.err.Error as e:
        return template('error.tpl', message='An error occurred. Error {!r}, errno is {}'.format(e, e.args[0]))

    return {'categories':categories,'message':''}

@route('/check_available_tools', method=['POST'])
@view('available_tools')
def check_avilable_tools_post():
    category = request.forms.get('category', '1').strip()
    print("category: " + str(category))
    start_date = datetime.datetime.strptime(request.forms.get('start_date', ''), '%m/%d/%Y')
    print("start: {:%b, %d %Y}".format(start_date))
    end_date = datetime.datetime.strptime(request.forms.get('end_date', ''), '%m/%d/%Y')
    print("end: {:%b, %d %Y}".format(end_date))
    
    try:
        tools = dbapi.get_available_tools(category, start_date, end_date)
    except pymysql.err.Error as e:
        return template('error.tpl', message='An error occurred. Error {!r}, errno is {}'.format(e, e.args[0]))

    for tool in tools:
        print("tool: " + str(tools))

    return {'tools':tools}
