from bottle import route, view, template, request, response, redirect
import pymysql.cursors
import pymysql.err
from database import dbapi


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
            connection = dbapi.connect()  # return db connection
            if connection == -1:
                return template('login.tpl')

            c = connection.cursor()

            sql = "INSERT INTO customers(email, first_name, last_name, password, address, work_phone_cc, work_phone_number, home_phone_cc, home_phone_number) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"

            c.execute(sql,(email, first_name, last_name, password, address, work_phone_cc, work_phone_number, home_phone_cc, home_phone_number))
            customer_id = c.lastrowid
            connection.commit()

        except pymysql.err.IntegrityError:
            return template('create_profile.tpl', message="The profile already exists.")
        except pymysql.err.Error as e:
            return template('login.tpl', message='An error occurred. Error {!r}, errno is {}'.format(e, e.args[0]))
        else:
            c.close()
            response.set_cookie("customer_id", str(customer_id))
            redirect('/customer_main_menu')
    else:
        return template('create_profile.tpl', message='')
