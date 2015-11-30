from app import *

class User (Model):
    username = CharField(unique=True)                               #Логин в Active Directory(LDAP)
    name = CharField()                                              #Имя
    surname = CharField()                                           #Фамилия
    birthday = DateField()                                          #День рождения
    position = CharField                                            #Должность
    phone = CharField()                                             #Номер телефона
    avatar = CharField()                                            #Имя аватора на сервере.
    mail = CharField()                                              #Электронная почта
    working_with = DateField()                                      #С какого времени работает.
    access_level = IntegerField()                                   #Уровень прав доступа к журналу
    time_started_h = IntegerField()                                 #Время начала работы
    time_started_m = IntegerField()
    end_time_work_h = IntegerField()                                #Время окончания работы
    end_time_work_m = IntegerField()

class Time_registarion(Model):
    username = CharField(unique=True)                               #Логин в Active Directory(LDAP)
    created_date = DateTimeField(default= datetime.datetime.now())  #Дата создания сообщения
    registration_status = IntegerField()                            #Регистрация = 1 разрегистрация = 0
    delay_reason = TextField()                                      #Причина опоздания