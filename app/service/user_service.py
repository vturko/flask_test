from collections import OrderedDict
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
SELECT_BY_NAME = 'SELECT * FROM user WHERE name="{}"'
INSERT_USER = 'INSERT INTO user ({}) VALUES ({});'


class UserService(BaseService):

    def select_all_users(self):
        select_result = self.sql_execute(USERS_SELECT, fetchall=True)

        users = []
        if select_result:
            for user in select_result:
                users.append({
                    'id': user[0],
                    'name': user[1],
                    'email': user[2],
                    'status': self.get_status(user[3])
                })

        return users

    def select_by_name(self, user_name):
        print 444444444, user_name
        select_result = self.sql_execute(SELECT_BY_NAME.format(user_name), fetchone=True)
        return select_result

    def add_user(self, user_data):
        print 3333333, user_data

        exist_in_db = self.select_by_name(user_data['name'])
        if exist_in_db:
            return 'User with name {} already exist!'

        user_json = self.repair_json(user_data)

        # user_json = OrderedDict(user_data)
        # print 55555555555, user_json
        # user_json['status'] = 1 if user_data['status'] == 'Active' else 0
        #
        # print 41414141, user_json, 41414, [x for x in user_json.itervalues()]
        #
        user_fields = (', ').join([x for x in user_json.keys()])
        user_values = (', ').join([x for x in user_json.itervalues()])
        sql = INSERT_USER.format(user_fields, user_values)
        print 5555555555, user_fields, 555555, user_values, 555, sql
        select_result = self.sql_execute(sql, commit=True)

        if select_result:
            return 'User with name {} added'

        return select_result

    def get_status(self, status_id):
        if not status_id:
            return 'Inactive'
        else:
            return 'Active'

    def repair_json(self, user_data):
        user_json = {x: '"' + user_data[x] + '"' for x in user_data if x}
        if user_json['status'] == '"Active"':
            user_json['status'] = '1'
        else:
            user_json['status'] = '0'

        return OrderedDict(user_json)
