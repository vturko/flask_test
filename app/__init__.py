from flask import Flask
import MySQLdb

app = Flask(__name__)
app.config.from_object('config')

# from app.views import views

DATABASE = app.config['DATABASE']

CONN = MySQLdb.connect(
    host=DATABASE['host'],
    user=DATABASE['username'],
    passwd=DATABASE['password'],
    db=DATABASE['database']
)