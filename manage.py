#!flask/bin/python

from app import app
from flask_script import Manager

from app.service.user_service import UserService

manager = Manager(app)

if __name__ == '__main__':
    manager.run()