from app import *
from datetime import datetime

class User (Model):
    username = CharField()                                                   #Логин в Active Directory(LDAP)
    name = CharField(null=True)                                              #Имя
    surname = CharField(null=True)                                           #Фамилия
    birthday = DateField(null=True)                                          #День рождения
    position = CharField(null=True)                                          #Должность
    phone = CharField(null=True)                                             #Номер телефона
    avatar = CharField(null=True)                                            #Имя аватора на сервере.
    mail = CharField(null=True)                                              #Электронная почта
    working_with = DateField(null=True)                                      #С какого времени работает.
    access_level = IntegerField(null=True)                                   #Уровень прав доступа к журналу
    time_started_h = IntegerField(null=True)                                 #Время начала работы
    time_started_m = IntegerField(null=True)
    end_time_work_h = IntegerField(null=True)                                #Время окончания работы
    end_time_work_m = IntegerField(null=True)

    class Meta:
        database=db

class Time_registarion(Model):
    username = CharField()                                                      #Логин в Active Directory(LDAP)
    created_date = DateTimeField()                      #Дата создания сообщения
    registration_status = IntegerField()                                        #Регистрация = 1 разрегистрация = 0
    delay_reason = TextField(null=True)                                         #Причина опоздания

    class Meta:
        database=db
