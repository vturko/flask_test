import re
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.fields.html5 import EmailField
# from wtforms_components import PhoneNumberField
from wtforms.validators import DataRequired, Email
from wtforms import ValidationError


class AddUserFrom(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    email = EmailField('email', validators=[DataRequired(), Email()])
    phone = StringField('phone')
    mobile = StringField('mobile')
    status = SelectField('status', choices=[('Inactive', 'Inactive'), ('Active', 'Active')])

    phone_templ_list = ['\d{11}$', '\d\(\d{3}\)\d{7}$', '\+\d{11}$', '\+\d\(\d{3}\)\d{7}$']

    def validate_phone(self, field):
        print 20202, field, 02020, type(field), 202020, str(field)
        print 30303030, field.data
        self.vnumber(field.data)

    def validate_mobile(self, field):
        print 20202, field, 02020, type(field), 202020, str(field)
        print 30303030, field.data
        self.vnumber(field.data)

    def vnumber(self, phone):
        if phone.strip():
            phone = phone.replace(' ', '').replace('-', '')

            is_valid_flag = False
            for phone_templ in self.phone_templ_list:
                if re.match(phone_templ, phone):
                    is_valid_flag = True

            print 40000000000000, is_valid_flag

            if not is_valid_flag:
                raise ValidationError('Invalid phone number. (11 digits)')

