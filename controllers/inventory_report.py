from bottle import route, view, template, request, response
import pymysql.cursors
import pymysql.err
import datetime
import calendar
from database import dbapi

@route('/inventory_report')
@view('inventory_report')
def generate_inventory_report():
    try:
        connection = dbapi.connect()
        c = connection.cursor()

        sql = "\
                SELECT \
                    t.tool_id, \
                    t.short_description, \
                    (t.day_price * COALESCE(rs.days_rented, 0)) AS rental_profit, \
                    (t.original_price + COALESCE(so.service_order_cost, 0)) AS cost_of_tool, \
                    ((t.day_price * COALESCE(rs.days_rented, 0)) - (t.original_price + COALESCE(so.service_order_cost, 0))) AS total_profit \
                FROM \
                    tools AS t \
                        LEFT JOIN ( \
                    SELECT tool_id, SUM(est_cost) service_order_cost \
                    FROM service_orders \
                    WHERE end_date < %s \
                    GROUP BY tool_id) so ON t.tool_id = so.tool_id \
                        LEFT JOIN ( \
                    SELECT rt.tool_id, SUM(DATEDIFF(r.end_date, r.start_date)) days_rented \
                    FROM reservations AS r JOIN reservations_tools AS rt ON r.reservation_id = rt.reservation_id \
                    WHERE r.end_date < %s \
                    GROUP BY rt.tool_id) rs ON t.tool_id = rs.tool_id \
                WHERE NOT EXISTS (SELECT * FROM sells WHERE t.tool_id = tool_id) \
                ORDER BY total_profit DESC"

        now = datetime.datetime.now()
        first_day_of_month = now.replace(day=1)
        last_day_of_month = now.replace(day=calendar.monthrange(now.year, now.month)[1])
        print("now: {:%b, %d %Y}".format(now))
        print("first: {:%b, %d %Y}".format(first_day_of_month))
        print("last : {:%b, %d %Y}".format(last_day_of_month))

        c.execute(sql, (last_day_of_month, last_day_of_month));
        #print('inventory_report: ' + str(c._last_executed))

        rows = c.fetchall()
        print(rows)
    except pymysql.err.Error as e:
        return template('error.tpl', message='An error occurred. Error {!r}, errno is {}'.format(e, e.args[0]))
    finally:
        c.close()

    return {'rows':rows}
