# -*- coding: utf-8 -*-
# Auther : jianlong
from db.user_dao import UserDao


class UserService(object):
    __user_dao = UserDao()

    def login(self, username, password):
        result = self.__user_dao.login(username, password)
        return result

    def search_user_role(self, username):
        role = self.__user_dao.search_user_role(username)
        return role

    def user_insert(self, username, password, email, role_id):
        self.__user_dao.user_insert(username, password, email, role_id)

    def search_list(self, page):
        return self.__user_dao.search_list(page)

    def search_page_count(self):
        return self.__user_dao.search_page_count()

    def user_delete(self, id):
        self.__user_dao.user_delete(id)

    def user_update(self, id, username, password, email, role_id):
        self.__user_dao.user_update(id, username, password, email, role_id)
