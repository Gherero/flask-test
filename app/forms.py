__author__ = 'gherero'
from flask_wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

class LoginForm(Form):
    surname = StringField('Фамилия:', validators=[DataRequired()])
    name = StringField('Имя:', validators=[DataRequired()])
    Middle_name = StringField('Отчество:', validators=[DataRequired()])
    internet = BooleanField('Интернет', default=False)
    mail=BooleanField("Почта",default=False)
    delo=BooleanField("Дело",default=False)
    #=BooleanField("",default=False)

    print("wine")
