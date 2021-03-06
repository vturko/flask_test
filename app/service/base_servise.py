import MySQLdb

from app import app

DATABASE = app.config['DATABASE']

CONN = MySQLdb.connect(
    host=DATABASE['host'],
    user=DATABASE['username'],
    passwd=DATABASE['password'],
    db=DATABASE['database']
)


class BaseService():

    def sql_execute(self, sql, fetchone=False, fetchall=False, commit=False):
        cur = CONN.cursor()
        try:
            cur.execute(sql)
            if fetchone:
                return cur.fetchone()
            elif fetchall:
                return cur.fetchall()
            elif commit:
                CONN.commit()
                return True

        except BaseException as e:
            if commit:
                CONN.rollback()
        finally:
            cur.close()
