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
                  'and %s = aes_decrypt(unhex(password),"HelloWorld")'
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
            sql = 'select tr.role from t_user u left join t_role tr on u.role_id = tr.id where u.username=%s'
            cursor.execute(sql, (username,))
            role = cursor.fetchone()[0]
            con.commit()
            return role
        except Exception as e:
            if 'con' in dir():
                con.rollback()
            print(e)
        finally:
            if 'con' in dir():
                con.close()

    def user_insert(self, username, password, email, role_id):
        try:
            con = my_pool.get_connection()
            con.start_transaction()
            cursor = con.cursor()
            sql = 'insert into t_user(username,password,email,role_id) values(%s,HEX(AES_ENCRYPT(%s,"HelloWorld")),%s,%s)'
            cursor.execute(sql, (username, password, email, role_id))
            con.commit()
        except Exception as e:
            if 'con' in dir():
                con.rollback()
            print(e)
        finally:
            if 'con' in dir():
                con.close()

    def search_page_count(self):
        try:
            con = my_pool.get_connection()
            cursor = con.cursor()
            sql = 'select ceil(count(*)/10) from t_user'
            cursor.execute(sql)
            count = cursor.fetchone()[0]
            return count
        except Exception as e:
            print(e)
        finally:
            if 'con' in dir():
                con.close()

    def search_list(self, page):
        try:
            con = my_pool.get_connection()
            con.start_transaction()
            cursor = con.cursor()
            sql = 'select u.id,u.username,r.role from t_user u ' \
                  'left join t_role r on u.role_id=r.id order by u.id ' \
                  'limit %s,%s'
            cursor.execute(sql, ((page - 1) * 10, 10))
            result = cursor.fetchall()
            con.commit()
            return result
        except Exception as e:
            print(e)
        finally:
            if 'con' in dir():
                con.close()

    def user_update(self, id, username, password, email, role_id):
        try:
            con = my_pool.get_connection()
            con.start_transaction()
            cursor = con.cursor()
            sql = 'update t_user set username=%s,password=HEX(AES_ENCRYPT(%s,"HelloWorld")),email=%s,role_id=%s where id=%s'
            cursor.execute(sql, (username, password, email, role_id, id))
            con.commit()
        except Exception as e:
            if 'con' in dir():
                con.rollback()
            print(e)
        finally:
            if 'con' in dir():
                con.close()

    def user_delete(self, username):
        try:
            con = my_pool.get_connection()
            con.start_transaction()
            cursor = con.cursor()
            sql = 'delete from t_user where id =%s'
            cursor.execute(sql, (id,))
            con.commit()
        except Exception as e:
            if 'con' in dir():
                con.rollback()
            print(e)
        finally:
            if 'con' in dir():
                con.close()

    def search_user_id(self, username):
        try:
            con = my_pool.get_connection()
            con.start_transaction()
            cursor = con.cursor()
            sql = 'select id from t_user where username = %s'
            cursor.execute(sql, (username,))
            user_id = cursor.fetchone()[0]
            con.commit()
            return user_id
        except Exception as e:
            if 'con' in dir():
                con.rollback()
            print(e)
        finally:
            if 'con' in dir():
                con.close()
