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
	category = request.forms.get('category', '1')
	requested_tool = request.forms.get("requested_tool", '')
	reserved_tools_field = request.forms.get('reserved_tools', '[]')

	try:
		categories = dbapi.get_categories()
		print("categories: " + str(categories))

		tools = dbapi.get_available_tools(category, start_date, end_date)

#		if request.forms.get('Add Tool', '').strip():
			# find the tool in the list of tools
#			for tool in tools:
#				print()
#				if str(tool['tool_id']) == requested_tool:
#					reserved_tools = eval(reserved_tools_field)
#					reserved_tools.append(tool)
#					reserved_tools_field = json.dumps(reserved_tools, default=decimal_default)
#					break

		print("reserved_tools_field: " + reserved_tools_field)

	except pymysql.err.Error as e:
		return template('error.tpl', message='An error occurred. Error {!r}, errno is {}'.format(e, e.args[0]))

	return {'start_date':start_date, 'end_date':end_date, 'categories':categories, 'tools':tools, 'selected_category':category, 'reserved_tools':reserved_tools_field, 'message':''}

def decimal_default(obj):
	if isinstance(obj, decimal.Decimal):
		return float(obj)
	raise TypeError

#json.dumps({'x': decimal.Decimal('5.5')}, default=decimal_default)