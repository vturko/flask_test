# from app import CONN
from base_servise import BaseService
# import MySQLdb
#
# from app import app
#
# DATABASE = app.config['DATABASE']
#
# CONN = MySQLdb.connect(
#     host=DATABASE['host'],
#     user=DATABASE['username'],
#     passwd=DATABASE['password'],
#     db=DATABASE['database']
# )
#
USERS_SELECT = 'SELECT * FROM user'


class UserService(BaseService):

    def select_all_users(self):
        select_result = self.sql_execute(USERS_SELECT, fetchall=True)

        users = []
        if select_result:
            for user in select_result:
                users.append({
                    'name': user[1],
                    'email': user[2],
                    'status': self.get_status(user[3])
                })

        return users

    def get_status(self, status_id):
        if not status_id:
            return 'Inactive'
        else:
            return 'Active'
