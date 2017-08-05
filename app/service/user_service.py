from app import CONN
from base_servise import BaseService

USERS_SELECT = 'SELECT * FROM user'


class UserService(BaseService):

    def select_all_users(self):
        select_result = self.sql_execute(USERS_SELECT, fetchall=True)

        if select_result:
            for user in select_result:
                print 111111111111, user
