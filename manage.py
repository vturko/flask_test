#!flask/bin/python

from app import app
from flask_script import Manager

from app.service.user_service import UserService

manager = Manager(app)

@manager.command
def select_all_user():
    u_s = UserService()
    u_s.select_all_users()


if __name__ == '__main__':
    manager.run()