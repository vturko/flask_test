from flask import request, render_template, redirect
from app import app
from app.service.user_service import UserService
from user_forms import AddUserFrom

@app.route('/')
@app.route('/index')
def index():
    return 'hello world'

@app.route('/users')
def users():
    user_s = UserService()
    users = user_s.select_all_users()
    return render_template('users.html', users=users)
    # return 'hello world'

# @app.route('/add_user/', methods=['GET', 'POST'])
# def add_user():
#     error = None
#     if request.method == 'POST':
#         if request.form:
#             user_s = UserService()
#             added = user_s.add_user(request.form)
#             if not added:
#                 error = 'User not added'
#             elif isinstance(added, str):
#                 error = added
#                 if 'User' in error:
#                     error = error.format(request.form['name'])
#         else:
#             error = 'Enter data, please'
#
#     return render_template('add_user.html', error_msg=error)

@app.route('/add_user/', methods=['GET', 'POST'])
def add_user():
    error = None
    form = AddUserFrom()

    print 141414141414 #, form.validate_on_submit()
    if request.method == 'POST' and form.validate_on_submit():
    # if form.validate_on_submit():
        print 2424242424
        if request.form:
            print 3434343434, request.form
            user_s = UserService()
            added = user_s.add_user(request.form)
            if not added:
                error = 'User not added'
            else:
                error = added
                if 'User' in error:
                    error = error.format(request.form['name'])

                return redirect("/users", code=302)

    return render_template('add_user.html', form=form, error_msg=error)
