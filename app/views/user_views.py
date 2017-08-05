from flask import request, render_template
from app import app
from app.service.user_service import UserService

@app.route('/')
@app.route('/index')
def index():
    return 'hello world'

@app.route('/users')
def users():
    user_s = UserService()
    users = user_s.select_all_users()
    print 222222222, users
    return render_template('users.html', users=users)
    # return 'hello world'

@app.route('/add_user/', methods=['GET', 'POST'])
def add_user():
    error = None
    if request.method == 'POST':
        if request.form:
            user_s = UserService()
            added = user_s.add_user(request.form)
            if not added:
                error = 'User not added'
            elif isinstance(added, str):
                error = added
                if 'User' in error:
                    error = error.format(request.form['name'])
        else:
            error = 'Enter data, please'

    return render_template('add_user.html', error=error)
