from bottle import route, view, template, request, response, redirect
import pymysql.cursors
import pymysql.err



@route('/customer_main_menu', method=['GET'])
@view('customer_main_menu')
def customer_main_menu():
    # Not sure if this is even needed
    pass
