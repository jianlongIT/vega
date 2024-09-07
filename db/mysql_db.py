# -*- coding: utf-8 -*-
# Auther : jianlong
from mysql.connector import pooling

__config = {
    'host': 'localhost',
    'port': 3306,
    'database': 'vega',
    'user': 'root',
    'password': 'Jianlong123.'
}

try:
    my_pool = pooling.MySQLConnectionPool(**__config, pool_size=10)
except Exception as e:
    print(e)
