__author__ = 'gherero'
from flask import Flask
from peewee import *
from datetime import datetime


db = PostgresqlDatabase('journal')
db.connect()

app = Flask(__name__)
app.config.from_object('config')


from app import controller