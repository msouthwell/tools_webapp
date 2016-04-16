from bottle import route, view, template, request, response
from controllers import utilities
import sys
import datetime

@route('/reservation_receipt/<reservation_id>', method=['POST'])
def reservation_receipt(reservation_id):

    reservation = utilities.view_reservation(reservation_id)
    tools = utilities.reservation_tools(reservation_id)
    data = reservation.copy()
    table = ""
    deposit= 0
    rental =0
    for row in tools:
        table= table+"<tr><td>{tool_id}</td><td>{short_description}</td></tr>".format(tool_id=row['tool_id'], short_description=row['short_description'])
        deposit += row['deposit']
        rental += row['day_price']
    data['tool_table'] = table
    data['deposit_required'] = deposit
    rental = rental * utilities.date_differance(reservation['start_date'], reservation['end_date'])
    data['estimated_cost'] = rental

    credit_card = request.forms.get('credit_card','').strip()
    expiration_date = request.forms.get('expiration_date','')
    expiration_date_datetime = datetime.datetime.strptime(expiration_date, '%m/%d/%Y')
    utilities.update_credit_card(reservation_id, credit_card, expiration_date_datetime)
    data['credit_card']= credit_card
    data['expiration_date']= expiration_date

    return template('reservation_receipt.tpl', data)