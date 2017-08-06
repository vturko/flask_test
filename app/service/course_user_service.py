from base_servise import BaseService

USERS_SELECT = 'SELECT * FROM courses JOIN course_user ON courses.id=course_user.course WHERE course_user.user={}'
COURSE_SELECT_AVAIL = 'SELECT * FROM courses WHERE id NOT IN (SELECT course AS id FROM courses JOIN course_user ' \
                    'ON courses.id=course_user.course WHERE course_user.user={})'
DELETE_USER_COURSE = 'DELETE FROM course_user WHERE user={} AND course={}'
COURSES_SELECT = 'SELECT * FROM courses'
SELECT_USER_COURSE = 'SELECT * FROM course_user WHERE user={} AND course={}'
INSERT_USER_COURSE = 'INSERT INTO course_user (user, course) VALUES ({}, {})'
SELECT_COUNT = 'SELECT COUNT(course) FROM course_user WHERE course_user.user={}'


class CourseUserService(BaseService):

    def select_all_courses(self):
        select_result = self.sql_execute(COURSES_SELECT, fetchall=True)

        return [(x[0], x[1]) for x in select_result]

    def select_all_av_courses(self, id):
        user_count = self.sql_execute(SELECT_COUNT.format(id), fetchone=True)
        if user_count[0] >= 5:
            return []

        select_result = self.sql_execute(COURSE_SELECT_AVAIL.format(id), fetchall=True)
        return [(x[0], x[1]) for x in select_result]

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

    def add_user_course(self, user_id, course_id):
        sql = SELECT_USER_COURSE.format(user_id, course_id)
        already_exist = self.sql_execute(sql, fetchone=True)
        if not already_exist:
            sql = INSERT_USER_COURSE.format(user_id, course_id)
            insert_result = self.sql_execute(sql, commit=True)
            return insert_result
        else:
            return 'User alredy get course'
