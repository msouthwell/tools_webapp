from bottle import route, view, template, request, response, redirect
import pymysql.cursors
import pymysql.err
import datetime
from database import dbapi


@route('/make_reservation', method=['GET'])
@view('make_reservation')
def view_make_reservation():
	try:
		categories = dbapi.get_categories()
		print("categories: " + str(categories))
	except pymysql.err.Error as e:
		return template('error.tpl', message='An error occurred. Error {!r}, errno is {}'.format(e, e.args[0]))

	return {'categories':categories,'message':''}
