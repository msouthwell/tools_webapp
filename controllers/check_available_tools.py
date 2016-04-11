from bottle import route, view, template, request, response, redirect
import pymysql.cursors
import pymysql.err


@route('/check_available_tools', method=['GET'])
@view('check_available_tools')
def check_avilable_tools_get():
    # Not sure if this is even needed
    pass

@route('/check_available_tools', method=['POST'])
@view('check_available_tools')
def check_avilable_tools_post():
    # Not sure if this is even needed
    pass
