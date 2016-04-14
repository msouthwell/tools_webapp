from bottle import route, view, template, request, response
from controllers import utilities
import sys

@route('/pick_up/<reservation_id>')
@view('pick_up')
def pick_up(reservation_id):
    # try:

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

    # except:
    #     return template('error.tpl', message='An error occurred in pick_up')
    # else:
        return data
