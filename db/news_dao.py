# -*- coding: utf-8 -*-
# Auther : jianlong
from db.mysql_db import my_pool


class NewsDao(object):
    def search_unreview_list(self, page):
        try:
            con = my_pool.get_connection()
            con.start_transaction()
            cursor = con.cursor()
            sql = 'select n.id,n.title,tt.type,u.username ' \
                  'from t_news as n left join t_type tt on n.type_id = tt.id ' \
                  'left join t_user as u on n.editor_id=u.id ' \
                  'where n.state=%s order by n.create_time desc ' \
                  'limit %s,%s'
            cursor.execute(sql, ("待审批", (page - 1) * 10, 10))
            result = cursor.fetchall()
            con.commit()
            return result
        except Exception as e:
            print(e)
        finally:
            if 'con' in dir():
                con.close()

    def search_unreview_count(self):
        try:
            con = my_pool.get_connection()
            con.start_transaction()
            cursor = con.cursor()
            sql = 'select ceil(count(*)/10) ' \
                  'from t_news as n where n.state=%s '
            cursor.execute(sql, ("待审批",))
            count = cursor.fetchone()[0]
            con.commit()
            return count
        except Exception as e:
            print(e)
        finally:
            if 'con' in dir():
                con.close()

    def update_unreview_count(self, id):
        try:
            con = my_pool.get_connection()
            con.start_transaction()
            cursor = con.cursor()
            sql = 'update t_news set state=%s where id =%s'
            cursor.execute(sql, ("已审批", id))
            con.commit()
        except Exception as e:
            if 'con' in dir():
                con.rollback()
            print(e)
        finally:
            if 'con' in dir():
                con.close()

    def search_list(self, page):
        try:
            con = my_pool.get_connection()
            con.start_transaction()
            cursor = con.cursor()
            sql = 'select n.id,n.title,tt.type,u.username ' \
                  'from t_news as n left join t_type tt on n.type_id = tt.id ' \
                  'left join t_user as u on n.editor_id=u.id order by n.create_time desc ' \
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

    def search_count_page(self):
        try:
            con = my_pool.get_connection()
            cursor = con.cursor()
            sql = 'select ceil(count(*)/10) from t_news'
            cursor.execute(sql)
            return cursor.fetone()[0]
        except Exception as e:
            print(e)
        finally:
            if 'con' in dir():
                con.close()

    def delete_new_by_id(self, new_id):
        try:
            con = my_pool.get_connection()
            con.start_transaction()
            cursor = con.cursor()
            delete_sql = 'delete from  t_news where new_id =%s'
            cursor.execute(delete_sql, (new_id,))
            con.commit()
        except Exception as e:
            if 'con' in dir():
                con.rollback()
            print(e)
        finally:
            if 'con' in dir():
                con.close()

    def insert(self, title, editor_id, type_id, content_id, is_top):
        try:
            con = my_pool.get_connection()
            con.start_transaction()
            cursor = con.cursor()
            insert_sql = 'insert into t_news(title, editor_id, type_id, content_id, is_top, state)' \
                         ' values(%s,%s,%s,%s,%s,%s)'
            cursor.execute(insert_sql, (title, editor_id, type_id, content_id, is_top, '待审批'))
            con.commit()
        except Exception as e:
            if 'con' in dir():
                con.rollback()
            print(e)
        finally:
            if 'con' in dir():
                con.close()
