# -*- coding: utf-8 -*-
# Auther : jianlong
from db.type_dao import TypeDao


class TypeService(object):
    __type_dao = TypeDao()

    def search_list(self):
        return self.__type_dao.searh_list()
