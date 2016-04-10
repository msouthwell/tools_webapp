from bottle import route, view, template, request, response, redirect
import pymysql.cursors
import pymysql.err
import os
import json


@route('/create_clerk', method=['GET','POST'])
@view('create_clerk')
def new_profile():
    if request.forms.get('Submit', '').strip():

        login = request.forms.get('login', '').strip()
        first_name = request.forms.get('first_name', '').strip()
        last_name = request.forms.get('last_name', '').strip()
        password = request.forms.get('password', '').strip()

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

            sql = "INSERT INTO clerks(login, first_name, last_name, password) VALUES (%s, %s, %s, %s)"

            c.execute(sql,(login, first_name, last_name, password))
            cust_id = c.lastrowid
            connection.commit()

        except pymysql.err.IntegrityError:
            return template('create_clerk.tpl', message="The clerk profile already exists.")
        except pymysql.err.Error as e:
            return template('login.tpl', message='An error occurred. Error {!r}, errno is {}'.format(e, e.args[0]))
        else:
            c.close()
            #return template('view_profile.tpl', message='New customer profile created.', cust_id=cust_id)
            redirect("/view_clerk/%s" % cust_id)
    else:
        return template('create_clerk.tpl', message='')
