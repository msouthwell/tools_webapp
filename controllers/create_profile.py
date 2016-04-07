from bottle import route, view, template, request, response, redirect
import pymysql.cursors
import pymysql.err
import os
import json


@route('/create_profile', method=['GET','POST'])
@view('create_profile')
def new_profile():
    if request.forms.get('Submit', '').strip():

        email = request.forms.get('email', '').strip()
        first_name = request.forms.get('first_name', '').strip()
        last_name = request.forms.get('last_name', '').strip()
        password = request.forms.get('password', '').strip()
        address = request.forms.get('address', '').strip()
        work_phone_cc = request.forms.get('work_phone_cc', '').strip()
        work_phone_number = request.forms.get('work_phone_number', '').strip()
        home_phone_cc = request.forms.get('home_phone_cc', '').strip()
        home_phone_number = request.forms.get('home_phone_number', '').strip()

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

            sql = "INSERT INTO customers(email, first_name, last_name, password, address, work_phone_cc, work_phone_number, home_phone_cc, home_phone_number) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"

            c.execute(sql,(email, first_name, last_name, password, address, work_phone_cc, work_phone_number, home_phone_cc, home_phone_number))
            cust_id = c.lastrowid
            connection.commit()

        except pymysql.err.IntegrityError:
            return template('create_profile.tpl', message="The profile already exists.")
        except pymysql.err.Error as e:
            return template('login.tpl', message='An error occurred. Error {!r}, errno is {}'.format(e, e.args[0]))
        else:
            c.close()
            #return template('view_profile.tpl', message='New customer profile created.', cust_id=cust_id)
            redirect("/view_profile/%s" % cust_id)
    else:
        return template('create_profile.tpl', message='')
