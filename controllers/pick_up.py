from bottle import route, view, template, request, response
from controllers import utilities

@route('/pick_up', method=['GET'])
@view('reservation_select')
def reservation_select():
    if request.GET.get('Submit', '').strip():
        id = request.GET.get('id', '').strip()
        return pick_up(id)
    else:
        return {'message': ''}

@route('/pick_up/<reservation_id>', method=['POST'])
@view('pick_up')
def pick_up(reservation_id):

    try:
        reservations = utilities.get_reservation_details(reservation_id)
        if len(reservations) != 1:
            return template('reservation_select', message='Could not find Reservation ' + str(reservation_id))
    except:
        return template('error.tpl', message='An error occurred in pick_up')

    return {'reservation':reservations[0], 'message':''}
