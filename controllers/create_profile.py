from bottle import route, view, template, request, response
import pymysql.cursors
import pymysql.err


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
            connection = pymysql.connect(host='localhost',
                                         db='test',
                                         user='root',
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
            return template('view_profile.tpl', message='New customer profile created.', cust_id=cust_id)

    else:
        return template('create_profile.tpl', message='')
