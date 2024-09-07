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


if __name__ == '__main__':
    pass
