from bottle import route, view, template, request, response
import pymysql.cursors

@route('/create_profile', method='GET')
def new_profile():
    if request.GET.get('Submit', '').strip():

        connection = pymysql.connect(host='localhost',
                             db='test',
                             user='root',
                             charset='utf8',
                             cursorclass=pymysql.cursors.DictCursor)

        c = connection.cursor()

        email = request.GET.get('email', '').strip()
        first_name = request.GET.get('first_name', '').strip()
        last_name = request.GET.get('last_name', '').strip()
        password = request.GET.get('password', '').strip()
        address = request.GET.get('address', '').strip()
        work_phone_cc = request.GET.get('work_phone_cc', '').strip()
        work_phone_number = request.GET.get('work_phone_number', '').strip()
        home_phone_cc = request.GET.get('home_phone_cc', '').strip()
        home_phone_number = request.GET.get('home_phone_number', '').strip()

        sql = "INSERT INTO customers(email, first_name, last_name, password, address, work_phone_cc, work_phone_number, home_phone_cc, home_phone_number) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"

        c.execute(sql,(email, first_name, last_name, password, address, work_phone_cc, work_phone_number, home_phone_cc, home_phone_number))
        cust_id = c.lastrowid

        connection.commit()
        c.close()

        return '<p>The new customer id is %s</p>' % cust_id
    else:
        return template('create_profile.tpl')
