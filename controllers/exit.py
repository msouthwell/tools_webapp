from bottle import route, view, template, request, response, redirect


@route('/exit', method=['GET', 'POST'])
@view('exit')
def view_login():
    response.delete_cookie("customer_id")
    response.delete_cookie("clerk_id")
    redirect('/login')
