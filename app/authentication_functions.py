
from datetime import datetime
import random
import hashlib
import redis
from flask import request
from ldap3 import Server, \
    Connection, \
    AUTO_BIND_NO_TLS, \
    SUBTREE, \
    ALL_ATTRIBUTES

redis_db = redis.StrictRedis(host='localhost', port=6379,db=0)

def magic_id(username):
    time=str(datetime.timestamp(datetime.now()))
    random_float_string= str(random.random())
    string = username + time + random_float_string
    string=string.encode()
    unique_id = hashlib.sha512(string).hexdigest()
    return unique_id

def get_username(session_id):
    username=redis_db.get(session_id)
    if not username == None:
        redis_db.expire(session_id,180)
    return username

def set_session(username,session_id):
    redis_db.set(session_id,username)
    redis_db.expire(session_id,1800)

def del_session():
    session_id = request.cookies.get('session_id')
    redis_db.delete(session_id)

def valid_session():
    session_id = request.cookies.get('session_id')
    print(session_id)
    username = get_username(session_id)
    return username

def get_ldap_info(username):
    with Connection(Server('192.168.73.35', port=636, use_ssl=True),
                    auto_bind=AUTO_BIND_NO_TLS,
                    read_only=True,
                    check_names=True,
                    user='ODESSA\\kshypachov', password='a roza upala na lapu azora') as c:

        c.search(search_base='CN=Users,DC=odessa,DC=gov,DC=ua',
                 search_filter='(&(samAccountName=' + username + '))',
                 search_scope=SUBTREE,
                 attributes=ALL_ATTRIBUTES,
                 get_operational_attributes=True)

    print(c.response_to_json())
    print(c.result)

