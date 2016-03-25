from bottle import route, view, request, response
from datetime import datetime

@route('/login')
@view('login')
def login():
    """Renders the login page"""
    return dict(
        title='Login',
        year=datetime.now().year
    )
