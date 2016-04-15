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

	return {'start_date':'','end_date':'','categories':categories, 'selected_category':categories[0]['category_id'], 'tools':(), 'message':''}

@route('/make_reservation', method=['POST'])
@view('make_reservation')
def make_reservation():
	print("Posting to make_reservation.")

	start_date = request.forms.get('start_date', '')
	end_date = request.forms.get('end_date', '')
	category = request.forms.get('category', '1')

	try:
		categories = dbapi.get_categories()
		print("categories: " + str(categories))

		tools = dbapi.get_available_tools(category, start_date, end_date)

	except pymysql.err.Error as e:
		return template('error.tpl', message='An error occurred. Error {!r}, errno is {}'.format(e, e.args[0]))

	return {'start_date':start_date,'end_date':end_date,'categories':categories, 'selected_category':category,'tools':tools,'message':''}
