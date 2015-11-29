__author__ = 'gherero'
from flask import Flask
from peewee import *

database = PostgresqlDatabase('journal')
database.connect()

app = Flask(__name__)
app.config.from_object('config')

from app import controller