__author__ = 'gherero'
from flask_wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

from flask.ext.wtf import Form
from wtforms import TextField, PasswordField, validators, HiddenField
from wtforms import TextAreaField, BooleanField
from wtforms.validators import Required, EqualTo, Optional
from wtforms.validators import Length, Email

from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required

class NameForm(Form):
    name = StringField()
    submit = SubmitField()

class LoginForm(Form):

    login=StringField(validators=[DataRequired()])
    passwrd=StringField()
    #surname = StringField('Фамилия:', validators=[DataRequired()])
    name = StringField('Имя:', validators=[DataRequired()])
    #Middle_name = StringField('Отчество:', validators=[DataRequired()])
    #internet = BooleanField('Интернет', default=False)
    #mail=BooleanField("Почта",default=False)
    #delo=BooleanField("Дело",default=False)
    #=BooleanField("",default=False)
    email = TextField('Email address', validators=[
           Required('Please provide a valid email address'),
           Length(min=6, message=(u'Email address too short')),
           Email(message=(u'That\'s not a valid email address.'))])


