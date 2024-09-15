# -*- coding: utf-8 -*-
# Auther : jianlong
from db.news_dao import NewsDao


class NewsService:
    __news_dao = NewsDao()

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
