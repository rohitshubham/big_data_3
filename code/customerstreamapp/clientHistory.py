#!/usr/bin/env python3

import redis

redis_host = "localhost"
redis_port = 6379
redis_password = ""
   
r = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)

def save_client_history(user_id, location, time):

    r.set(user_id, str((location, time)))

def get_client_history(user_id):
    return r.get(user_id)

def does_user_exist(user_id):
    return r.exists(user_id) != 0


