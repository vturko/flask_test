from flask import render_template, flash, redirect
from app import app
from app.service.user_service import UserService

@app.route('/')
@app.route('/index')
def index():
    return 'hello world'

@app.route('/users')
def users():
    u_s = UserService()
    users = u_s.select_all_users()
    print 222222222, users
    return render_template('users.html', users=users)
    # return 'hello world'

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     form = LoginFrom()
#     if form.validate_on_submit():
#         flash('Login request for openID="' + form.openid.data +
#               '", remember_me=' + str(form.rememeber_me.data))
#
#         return redirect('./index')
#
#     return render_template('login.html', title="Sign In", form=form,
#                            providers=app.config['OPENID_PROVIDERS'])
