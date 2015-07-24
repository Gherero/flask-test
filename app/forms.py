__author__ = 'gherero'
from flask_wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

class LoginForm(Form):
    TestString = StringField('openid', validators=[DataRequired()])
    TestBool = BooleanField('bolean', default=False)
    print("wine")
