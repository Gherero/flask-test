from datetime import datetime
import random
import hashlib
import redis

redis_db = redis.StrictRedis(host='localhost', port=6379,db=0)

def magic_id(username):
    time=str(datetime.timestamp(datetime.now()))
    random_float_string= str(random.random())
    string = username + time + random_float_string
    string=string.encode()
    unique_id = hashlib.sha512(string).hexdigest()
    return unique_id

def get_session(session_id):
    username=redis_db.get(session_id)
    return username

def set_session(username,session_id):
    if not redis_db.exists(username):
        redis_db.set(session_id,username)
    redis_db.expire(session_id,1800)

def del_session(session_id):
    redis_db.delete(session_id)
