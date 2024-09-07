# -*- coding: utf-8 -*-
# Auther : jianlong
from db.user_dao import UserDao


class UserService(object):
    __user_dao = UserDao()


if __name__ == '__main__':
    pass
