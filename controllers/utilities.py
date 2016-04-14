
from bottle import template

def view_reservation(reservation_id):

    try:
        connection = dbapi.connect()
        if connection == -1:
            return template('error.tpl', message="Database could not connect");

        c = connection.cursor()

        sql = "SELECT * FROM RESERVATIONS " \
            "WHERE reservation_id = %s"
        print(sql, reservation_id)
        c.execute(sql, reservation_id)
        data= c.fetchone()
        c.close()
    except pymysql.err.Error as e:
        return template('error.tpl', message='An error occurred. Error {!r}, errno is {}'.format(e, e.args[0]))
    else:
        return data