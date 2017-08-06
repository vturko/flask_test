# from collections import OrderedDict
from base_servise import BaseService

USERS_SELECT = 'SELECT * FROM courses JOIN course_user ON courses.id=course_user.course WHERE course_user.user={}'
DELETE_USER_COURSE = 'DELETE FROM course_user WHERE user={} AND course={}'
# SELECT_BY_ID = 'SELECT * FROM user WHERE id="{}"'
# SELECT_BY_NAME = 'SELECT * FROM user WHERE name="{}"'
# INSERT_USER = 'INSERT INTO user ({}) VALUES ({});'
# UPDATE_USER = 'UPDATE user SET {} WHERE id="{}"'
# DELETE_BY_ID = 'DELETE FROM user WHERE id={}'


class CourseUserService(BaseService):

    def select_by_user_id(self, user_id):
        select_result = self.sql_execute(USERS_SELECT.format(user_id), fetchall=True)

        courses_list = []
        for course in select_result:
            courses_list.append({
                'id': course[0],
                'name': course[1]
            })

        return courses_list

    def delete_user_course(self, user_id, course_id):
        sql = DELETE_USER_COURSE.format(user_id, course_id)

        return self.sql_execute(sql, commit=True)
