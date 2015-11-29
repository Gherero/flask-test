from app import *

class User (Model):
    username = CharField(unique=True,primary_key=True,null=False)   #Логин в Active Directory(LDAP)
    name = CharField()                                              #Имя
    surname = CharField()                                           #Фамилия
    birthday = DateField()                                          #День рождения
    position = CharField                                            #Должность
    phone = CharField()                                             #Номер телефона
    avatar = CharField()                                            #Имя аватора на сервере.
    mail = CharField()                                              #Электронная почта
    working_with = DateField()                                      #С какого времени работает.
