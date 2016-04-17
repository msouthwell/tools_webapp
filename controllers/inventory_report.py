from bottle import route, view, template, request, response
import pymysql.cursors
import pymysql.err
from database import dbapi

@route('/inventory_report')
@view('inventory_report')
def generate_inventory_report():
    try:
        connection = dbapi.connect()
        c = connection.cursor()

        c.execute("SELECT T.tool_id, T.short_description, \
                  COALESCE( SUM( DATEDIFF(R.end_date, R.start_date)*T.day_price), 0) \
                  AS rental_profit, \
                  (T.original_price + COALESCE (SUM(SO.est_cost),0)) AS cost_of_tool, \
                  (COALESCE( SUM( DATEDIFF(R.end_date, R.start_date)*T.day_price), 0) - \
                  T.original_price + COALESCE (SUM(SO.est_cost),0)) AS total_profit \
                  FROM \
                  TOOLS AS T \
                  LEFT JOIN RESERVATIONS_TOOLS AS RT ON T.tool_id=RT.tool_id \
                  LEFT JOIN RESERVATIONS AS R ON R.reservation_id=RT.reservation_id \
                  LEFT JOIN SERVICE_ORDERS AS SO ON SO.tool_id = T.tool_id \
                  WHERE \
                  NOT EXISTS ( \
                  SELECT T.tool_id \
                  FROM SELLS AS S \
                  WHERE sale_date < NOW() AND T.tool_id=S.tool_id ) \
                  GROUP BY T.tool_id \
                  ORDER BY total_profit DESC" )

        rows = c.fetchall()
        print(rows)
    except pymysql.err.Error as e:
        return template('error.tpl', message='An error occurred. Error {!r}, errno is {}'.format(e, e.args[0]))
    finally:
        c.close()

    return template('inventory_report', rows=rows)
