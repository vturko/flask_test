from collections import OrderedDict
from base_servise import BaseService

USERS_SELECT = 'SELECT * FROM user'
SELECT_BY_ID = 'SELECT * FROM user WHERE id="{}"'
SELECT_BY_NAME = 'SELECT * FROM user WHERE name="{}"'
INSERT_USER = 'INSERT INTO user ({}) VALUES ({});'
UPDATE_USER = 'UPDATE user SET {} WHERE id="{}"'
DELETE_BY_ID = 'DELETE FROM user WHERE id={}'


class UserService(BaseService):
    user_field_list = ['id', 'name', 'email', 'status', 'phone', 'mobile']

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

    def get_user_by_id(self, user_id):
        user_value_list = self.select_by_id(user_id)
        user_json = {x: y for x, y in zip(self.user_field_list, user_value_list)}
        if user_json['status']:
            user_json['status'] = 'Active'
        else:
            user_json['status'] = 'Inactive'

        for user_el in user_json:
            if not user_json[user_el]:
                user_json[user_el] = ''

        return user_json

    def select_by_id(self, user_id):
        select_result = self.sql_execute(SELECT_BY_ID.format(user_id), fetchone=True)
        return select_result

    def select_by_name(self, user_name):
        select_result = self.sql_execute(SELECT_BY_NAME.format(user_name), fetchone=True)
        return select_result

    def add_user(self, user_data):
        exist_in_db = self.select_by_name(user_data['name'])
        if exist_in_db:
            return 'User with name {} already exist!'

        user_json = self.repair_json(user_data)

        user_fields = (', ').join([x for x in user_json.keys()])
        user_values = (', ').join([x for x in user_json.itervalues()])
        sql = INSERT_USER.format(user_fields, user_values)
        select_result = self.sql_execute(sql, commit=True)

        if select_result:
            return 'User with name {} added'

        return select_result

    def update_user(self, id, user_data):
        old_json = self.get_user_by_id(id)
        new_json = {x: user_data[x] for x in user_data}
        update_json = {}
        for n_key in new_json:
            if n_key in old_json and new_json[n_key] != old_json[n_key]:
                update_json[n_key] = new_json[n_key]

        update_str = ''
        for u_key in update_json:
            u_val = update_json[u_key]
            if u_key == 'status':
                u_val = self.get_status_code(u_val)
            if u_key in ['phone', 'mobile']:
                u_val = self.get_phone_digits(u_val)

            update_str += u_key + '="' + u_val + '", '

        if update_str:
            update_str = update_str[:-2]
            sql = UPDATE_USER.format(update_str, id)
            update_result = self.sql_execute(sql, commit=True)
            if update_result:
                return "User data updated"
            else:
                return update_result
        else:
            return "All data upp to date"

    def delete_user(self, id):
        user = self.select_by_id(id)
        sql = DELETE_BY_ID.format(id)
        del_result = self.sql_execute(sql, commit=True)
        if del_result:
            return 'User "{}" deleted'.format(user[1])
        else:
            return del_result

    def get_status(self, status_id):
        if not status_id:
            return 'Inactive'
        else:
            return 'Active'

    def repair_json(self, user_data):
        user_data_list = ['name', 'email', 'phone', 'mobile', 'status']
        user_json = {x: '"' + user_data[x] + '"' for x in user_data if x in user_data_list and user_data[x]}

        user_json['status'] = self.get_status_code(user_json['status'])

        for ph_el in ['phone', 'mobile']:
            if ph_el in user_json:
                user_json[ph_el] = self.get_phone_digits(user_json[ph_el])

        return OrderedDict(user_json)

    def get_status_code(self, user_status):
        return '1' if user_status == '"Active"' else '0'

    def get_phone_digits(self, phone_number):
        return phone_number.replace('+', '').replace('(', '').replace(')', '')