from flask import request, render_template, redirect, url_for
from app import app
from app.service.user_service import UserService
from app.service.course_user_service import CourseUserService
from user_forms import AddUserFrom#, ChangeUserForm

@app.route('/')
@app.route('/index')
def index():
    return 'hello world'

@app.route('/users')
def users():
    message = None
    if 'message' in request.args:
        message = request.args['message']
    print 888888, message
    user_s = UserService()
    users = user_s.select_all_users()
    return render_template('users.html', users=users, message=message)

@app.route('/delete/<int:id>', methods=['POST'])
def delete_user(id):
    print 4545454545, id
    user_s = UserService()
    deleted = user_s.delete_user(id)
    if not deleted:
        deleted = "User wasn't deleted"
    # return redirect('/users')
    return redirect(url_for('.users', message=deleted))

@app.route('/add_user/', methods=['GET', 'POST'])
def add_user():
    error = None
    confirm = None
    form = AddUserFrom()

    if request.method == 'POST' and form.validate_on_submit():
        if request.form:
            user_s = UserService()
            added = user_s.add_user(request.form)
            if not added:
                error = 'User not added'
            elif 'already exist' in added:
                error = added.format(request.form['name'])
            else:
                confirm = added
                if 'User' in confirm:
                    confirm = confirm.format(request.form['name'])

    return render_template('add_user.html', form=form, error_msg=error, confirm_msg=confirm)

@app.route('/change_user/<int:id>', methods=['GET' ,'POST'])
def change_user(id):
    error = None
    confirm = None
    user_s = UserService()
    user = user_s.get_user_by_id(id)

    form = AddUserFrom(status=user['status'])
    course_u = CourseUserService()
    user_courses = course_u.select_by_user_id(id)

    if request.method == 'POST' and form.validate_on_submit():
        if request.form:
            print 828282828, request.form
            user_s = UserService()
            updated = user_s.update_user(id, request.form)

            if not updated:
                error = 'Info not updated'
            else:
                confirm = updated

            user = user_s.get_user_by_id(id)

    return render_template('change_user.html', user=user, form=form,
                           error_msg=error, confirm_msg=confirm,
                           user_courses=user_courses)

@app.route('/delete_user_course', methods=['POST'])
def delete_course_user():
    print request.form['course_id']

    course_u = CourseUserService()
    course_u.delete_user_course(request.form['user_id'], request.form['course_id'])

    return redirect(url_for('.change_user', id=request.form['user_id']))
