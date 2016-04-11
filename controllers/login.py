from bottle import route, view, template, request, response, redirect
import pymysql.cursors
import pymysql.err
import os
import json


@route('/login', method=['GET', 'POST'])
@view('login')
def login():
    if request.forms.get('Submit', '').strip():
        login = request.forms.get('login', '').strip()
        password = request.forms.get('password', '').strip()
        user_type = request.forms.get('usertype', '').strip()

        #TODO refactor this out into a seperate datbase class
        try:
            # Specify config in database.json or editing 'database' variable below
            db_config_file = os.path.join(os.path.dirname(__file__), "database.json")

            if os.path.exists(db_config_file):
                with open(db_config_file) as f:
                    database = json.load(f)
            else:
                    database = [ {"host":"localhost", "db":"test", "user":"root", "passwd":""}]

            connection = pymysql.connect(host=database[0]['host'],
                                         user=database[0]['user'],
                                         passwd=database[0]['passwd'],
                                         db=database[0]['db'],
                                         charset='utf8',
                                         cursorclass=pymysql.cursors.DictCursor)

            c = connection.cursor()
            if user_type == "clerks":
                sql = "SELECT login, password FROM clerks WHERE login=%s"
            elif user_type == "customers":
                sql = "SELECT email, password FROM customers WHERE email=%s"
            c.execute(sql, login)  # login or email

            result = c.fetchone()

            if result is None:
                return template('login.tpl', message='Email or password incorrect')

            connection.commit() # why commit?
            c.close()

        except pymysql.err.Error as e:
            return template('login.tpl', message='An error occurred. Error {!r}, errno is {}'.format(e, e.args[0]))

        if password == result['password']:
            if user_type == "clerks":
                redirect('/clerk_main_menu')
            elif user_type == "customers":
                redirect('/customer_main_menu')
        else:
            return template('login.tpl', message='Email or password incorrect')

    else:
        return template('login.tpl', message='Enter email and password')
