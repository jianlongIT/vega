# -*- coding: utf-8 -*-
# Auther : jianlong
from db.news_dao import NewsDao
from db.redis_news_dao import RedisNewsDao


class NewsService:
    __news_dao = NewsDao()
    __redis_news_dao = RedisNewsDao()

    def search_unreview_list(self, page):
        result = self.__news_dao.search_unreview_list(page)
        return result

    def search_unreview_page_count(self):
        count_page = self.__news_dao.search_unreview_count()
        return count_page

    # 审批新闻
    def update_unreview_count(self, id):
        self.__news_dao.update_unreview_count(id)

    # 查询列表
    def search_list(self, page):
        result = self.__news_dao.search_list(page)
        return result

    # 查询新闻总页数
    def search_count_page(self):
        count = self.__news_dao.search_count_page()
        return count

    def delete_new_by_id(self, new_id):
        self.__news_dao.delete_new_by_id(new_id)

    def insert(self, title, editor_id, type_id, content_id, is_top):
        self.__news_dao.insert(title, editor_id, type_id, content_id, is_top)

    def search_cache(self, id):
        return self.__news_dao.search_cache(id)

    def cache_news(self, id, title, username, type, content, is_top, create_time):
        self.__redis_news_dao.insert(id, title, username, type, content, is_top, create_time)

    def cache_delete(self, id):
        self.__redis_news_dao.delete(id)

    def search_by_id(self, id):
        return self.__news_dao.search_by_id(id)

    def new_update(self, id, title, type_id, content_id, is_top):
        self.__news_dao.new_update(id, title, type_id, content_id, is_top)
        self.__redis_news_dao.delete(id)
