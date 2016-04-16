from bottle import route, view, template, request, response, redirect
import pymysql.cursors
import pymysql.err
import datetime
import json
import decimal
from database import dbapi


@route('/make_reservation', method=['GET'])
@view('make_reservation')
def view_make_reservation():
	try:
		categories = dbapi.get_categories()
		print("categories: " + str(categories))
	except pymysql.err.Error as e:
		return template('error.tpl', message='An error occurred. Error {!r}, errno is {}'.format(e, e.args[0]))

	return {'start_date':'', 'end_date':'', 'categories':categories, 'tools':(), 'selected_category':categories[0]['category_id'], 'reserved_tools':'[]', 'message':''}

@route('/make_reservation', method=['POST'])
@view('make_reservation')
def make_reservation():
	print("Posting to make_reservation.")
	start_date = request.forms.get('start_date', '')
	end_date = request.forms.get('end_date', '')
	reserved_tools_field = request.forms.get('reserved_tools', '[]')

	if request.forms.get('Calculate Total', '').strip():
		print ('Calculating total for: ' + reserved_tools_field)
		reserved_tools = eval(reserved_tools_field)

		deposit = 0.0
		rental_price = 0.0

		for reserved_tool in reserved_tools:
			deposit += reserved_tool['deposit']
			rental_price += reserved_tool['day_price']

		return template('reservation_summary.tpl', reserved_tools=reserved_tools, start_date=start_date, end_date=end_date, rental_price=rental_price, deposit=deposit)

	elif request.forms.get('Reserve Tools', '').strip():
		reserved_tools = eval(reserved_tools_field)

		if len(reserved_tools) < 1 or len(reserved_tools) > 50:
			category = request.forms.get('category', '1')
			tools = dbapi.get_available_tools(category, start_date, end_date)

			return {'start_date':start_date, 'end_date':end_date, 'categories':dbapi.get_categories(), 'tools':tools, 'selected_category':category, 'reserved_tools':reserved_tools_field, 'message':'Only 1 to 50 tools can be reserved at a time.'}

		no_longer_availables = dbapi.check_available_tools(reserved_tools, start_date, end_date)
		if len(no_longer_availables) > 0:
			category = request.forms.get('category', '1')
			tools = dbapi.get_available_tools(category, start_date, end_date)

			tool_message = ''
			for no_longer_available in no_longer_availables:
				if len(tool_message) > 0:
					tool_message += ', '
				tool_message += no_longer_available['short_description']

			return {'start_date':start_date, 'end_date':end_date, 'categories':dbapi.get_categories(), 'tools':tools, 'selected_category':category, 'reserved_tools':reserved_tools_field, 'message':'The following tools are no longer available: ' + tool_message}

		start_date_value = datetime.datetime.strptime(start_date, '%m/%d/%Y')
		end_date_value = datetime.datetime.strptime(end_date, '%m/%d/%Y')
		customer_id = int(request.get_cookie('customer_id'))

		try:
			connection = dbapi.connect()  # return db connection

			c = connection.cursor()

			c.execute("INSERT INTO reservations(customer_id, start_date, end_date) VALUES(%s, %s, %s)", (customer_id, start_date_value, end_date_value))
			reservation_id = c.lastrowid

			reserved_tools = eval(reserved_tools_field)
			for reserved_tool in reserved_tools:
				c.execute("INSERT INTO reservations_tools(reservation_id, tool_id) VALUES(%s, %s)", (reservation_id, reserved_tool['tool_id']))

			connection.commit()

		except pymysql.err.Error as e:
			return template('error.tpl', message='An error occurred. Error {!r}, errno is {}'.format(e, e.args[0]))
		finally:
			c.close() # make sure the connection gets closed

		redirect('/view_reservation/%s' % reservation_id)

	else:
		category = request.forms.get('category', '1')

		try:
			categories = dbapi.get_categories()
			print("categories: " + str(categories))

			tools = dbapi.get_available_tools(category, start_date, end_date)

		except pymysql.err.Error as e:
			return template('error.tpl', message='An error occurred. Error {!r}, errno is {}'.format(e, e.args[0]))

		return {'start_date':start_date, 'end_date':end_date, 'categories':categories, 'tools':tools, 'selected_category':category, 'reserved_tools':reserved_tools_field, 'message':''}

def decimal_default(obj):
	if isinstance(obj, decimal.Decimal):
		return float(obj)
	raise TypeError
