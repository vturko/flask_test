from flask import request, render_template, redirect, url_for
from app import app
from app.service.user_service import UserService
from app.service.course_user_service import CourseUserService
from user_forms import AddUserFrom, CourseForm


@app.route('/users')
def users():
    message = None
    if 'message' in request.args:
        message = request.args['message']
    user_s = UserService()
    users = user_s.select_all_users()
    return render_template('users.html', users=users, message=message)


@app.route('/delete/<int:id>', methods=['POST'])
def delete_user(id):
    user_s = UserService()
    deleted = user_s.delete_user(id)
    if not deleted:
        deleted = "User wasn't deleted"
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


@app.route('/change_user/<int:id>', methods=['GET', 'POST'])
def change_user(id):
    error = None
    confirm = None
    user_s = UserService()
    user = user_s.get_user_by_id(id)

    form = AddUserFrom(status=user['status'])
    form_course = CourseForm()
    course_u = CourseUserService()
    user_courses = course_u.select_by_user_id(id)
    all_av_courses = course_u.select_all_av_courses(id)
    has_avail = True if all_av_courses else False
    form_course.courses.choices = all_av_courses

    if request.method == 'POST' and form.validate_on_submit():
        if request.form:
            user_s = UserService()
            updated = user_s.update_user(id, request.form)

            if not updated:
                error = 'Info not updated'
            else:
                confirm = updated

            user = user_s.get_user_by_id(id)

    return render_template('change_user.html', user=user, form=form, form_course=form_course,
                           error_msg=error, confirm_msg=confirm,
                           user_courses=user_courses, has_avail=has_avail)


@app.route('/delete_user_course', methods=['POST'])
def delete_course_user():
    course_u = CourseUserService()
    course_u.delete_user_course(request.form['user_id'], request.form['course_id'])

    return redirect(url_for('.change_user', id=request.form['user_id']))


@app.route('/add_course/<int:user_id>', methods=['GET', 'POST'])
def add_course(user_id):
    course_id = request.form['courses']
    course_u = CourseUserService()
    course_u.add_user_course(user_id, course_id)

    return redirect(url_for('.change_user', id=user_id))
