from bottle import route, view, template, request, response, redirect


@route('/clerk_main_menu', method=['GET'])
@view('clerk_main_menu')
def clerk_main_menu():
    # Not sure if this is even needed
    pass
