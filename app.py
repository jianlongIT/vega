# -*- coding: utf-8 -*-
# Auther : jianlong
from colorama import Back, Fore, Style
from getpass import getpass
from service.user_service import UserService
import os, sys

__user_service = UserService()
if __name__ == '__main__':
    while True:
        os.system('clear')
        print(Fore.LIGHTBLUE_EX, '\n\t========================================')
        print(Fore.LIGHTBLUE_EX, '\n\t============欢迎使用新闻管理系统============')
        print(Fore.LIGHTBLUE_EX, '\n\t========================================')
        print(Fore.LIGHTGREEN_EX, '\n\t1.登录系统')
        print(Fore.LIGHTGREEN_EX, '\n\t2.退出系统')
        print(Style.RESET_ALL)
        opt = input('\n\t输入操作编号:')
        if opt == '1':
            username = input('\n\t用户名:')
            password = getpass('\n\t密码:')
            result = __user_service.login(username, password)
            if result:
                role = __user_service.search_user_role(username)
                os.system('clear')
                print(role)
                while True:
                    if role == '新闻编辑':
                        pass
                    elif role == '管理员':
                        print(Fore.LIGHTBLUE_EX, '\n\t1.新闻管理')
                        print(Fore.LIGHTBLUE_EX, '\n\t2.用户管理')
                        print(Fore.LIGHTRED_EX, '\n\tback.退出登录')
                        print(Fore.LIGHTRED_EX, '\n\texit.退出系统')
                        choice = input('选择')
                        if choice == 'exit':
                            exit()


        elif opt == '2':
            sys.exit()
