# -*- coding: utf-8 -*-
# Auther : jianlong
from db.mysql_db import my_pool


class TypeDao(object):

    def searh_list(self):
        try:
            con = my_pool.get_connection()
            con.start_transaction()
            cursor = con.cursor()
            sql = 'select id,type from t_type order by id'
            cursor.execute(sql)
            result = cursor.fetchall()
            con.commit()
            return result
        except Exception as e:
            print(e)
        finally:
            if 'con' in dir():
                con.close()
