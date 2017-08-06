import re
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.fields.html5 import EmailField
# from wtforms_components import PhoneNumberField
from wtforms.validators import DataRequired, Email, Regexp
from wtforms import ValidationError


class AddUserFrom(FlaskForm):
    name = StringField('name', validators=[DataRequired(), Regexp('^[A-Za-z ]*$', 0,
                                                                  'Usernames must have only letters or spaces')])
    email = EmailField('email', validators=[DataRequired(), Email()])
    phone = StringField('phone')
    mobile = StringField('mobile')
    status = SelectField('status', choices=[('Inactive', 'Inactive'), ('Active', 'Active')])

    phone_templ_list = ['\d{11}$', '\d\(\d{3}\)\d{7}$', '\+\d{11}$', '\+\d\(\d{3}\)\d{7}$']

    def validate_phone(self, field):
        self.vnumber(field.data)

    def validate_mobile(self, field):
        self.vnumber(field.data)

    def vnumber(self, phone):
        if phone and phone.strip():
            phone = phone.replace(' ', '').replace('-', '')

            is_valid_flag = False
            for phone_templ in self.phone_templ_list:
                if re.match(phone_templ, phone):
                    is_valid_flag = True

            if not is_valid_flag:
                raise ValidationError('Invalid phone number. (11 digits)')
