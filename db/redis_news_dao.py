# -*- coding: utf-8 -*-
# Auther : jianlong
from redis import Redis
from db.redis_db import redis_pool


class RedisNewsDao(object):

    def insert(self, id, title, username, type, content, is_top, create_time):
        con = Redis(connection_pool=redis_pool)
        try:
            con.hset(id, mapping={
                'title': title,
                'author': username,
                'type': type,
                'content': content,
                'is_top': is_top,
                'create_time': create_time
            })
            if is_top == 0:
                con.expire(id, 3600 * 24)
        except Exception as e:
            print(e)
        finally:
            if con in dir():
                del con

    def delete(self, id):
        con = Redis(connection_pool=redis_pool)
        try:
            con.delete(id)
        except Exception as e:
            print(e)
        finally:
            del con
