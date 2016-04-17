from bottle import route, view, template, request, response, redirect
import pymysql.err
import datetime
from database import dbapi
from controllers import utilities


@route('/view_reservation/<reservation_id>', method=['GET'])
@view('view_reservation')
def view_reservation(reservation_id):
	print('Viewing reservation ' + reservation_id)
	reservations = utilities.get_reservation_details(reservation_id)
	if len(reservations) != 1:
		return {'reservations':'', 'message':'Could not find Reservation ' + str(reservation_id)}

	return {'reservations':reservations, 'message':''}

@route('/view_reservation/customer/<customer_id>', method=['GET'])
@view('view_reservation')
def view_reservation_customer(customer_id):
	print('Viewing reservation for customer' + customer_id)
	reservations = utilities.get_reservation_details_by_customer(customer_id)
	if len(reservations) == 0:
		return {'reservations':'', 'message':'Could not find Reservation for Customer ' + str(customer_id)}

	return {'reservations':reservations, 'message':''}
