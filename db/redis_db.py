# -*- coding: utf-8 -*-
# Auther : jianlong
from redis import Redis, ConnectionPool

try:
    redis_pool = ConnectionPool(
        host='localhost',
        port='6379',
        db='1',
        max_connections=20
    )
except Exception  as e:
    print(e)
