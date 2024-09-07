# -*- coding: utf-8 -*-
# Auther : jianlong
from db.mysql_db import my_pool


class UserDao(object):
    def login(self, username, password):
        try:
            con = my_pool.get_connection()
            con.start_transaction()
            cursor = con.cursor()
            sql = 'select count(*) from t_user where username=%s ' \
                  'and %s = aes_decrypt(unhex(password),"jianlong")'
            cursor.execute(sql, (username, password))
            count = cursor.fetchone()[0]
            con.commit()
            return count == 1
        except Exception as e:
            print(e)
        finally:
            if 'con' in dir():
                con.close()

    # 查询用户角色
    def search_user_role(self, username):
        try:
            con = my_pool.get_connection()
            con.start_transaction()
            cursor = con.cursor()
            sql = 'select tr.role from t_user u left join t_role tr on u.role_id = tr.id'
            'where u.username=%s'
            cursor.execute(sql, (username,))
            con.commit()
            role = cursor.fetchone()[0]
            return role
        except Exception as e:
            if 'con' in dir():
                con.rollback()
            print(e)
        finally:
            if 'con' in dir():
                con.close()
