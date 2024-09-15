# -*- coding: utf-8 -*-
# Auther : jianlong
from db.role_dao import RoleDao


class RoleService(object):
    __role_dao = RoleDao()

    def search_list(self):
        return self.__role_dao.search_list()
