# -*- coding: utf-8 -*-
# Auther : jianlong
from colorama import Back, Fore, Style
from getpass import getpass
from service.user_service import UserService
from service.news_service import NewsService
from service.role_service import RoleService
import os, sys, time

__user_service = UserService()
__news_service = NewsService()
__role_srvice = RoleService()


def show_list(result, current_page):
    for index, value in enumerate(result):
        print(Fore.LIGHTBLUE_EX,
              '\n\t%d\t%s\t%s\t%s' % (index + 1, value[1], value[2], value[3]))
    print(Fore.LIGHTBLUE_EX, '\n\t========================================')
    print(Fore.LIGHTBLUE_EX, '\n\t当前在第%d页 共%d页' % (current_page, count_page))
    print(Fore.LIGHTBLUE_EX, '\n\t========================================')
    print(Fore.LIGHTRED_EX, '\n\tback.返回上一层')
    print(Fore.LIGHTRED_EX, '\n\tprev.上一页')
    print(Fore.LIGHTRED_EX, '\n\tnext.下一页')
    print(Style.RESET_ALL)
    opt = input('\n\t输入操作编号:')
    if opt == 'back':
        break_flag = True
    if opt == 'next' and current_page < count_page:
        current_page += 1
    if opt == 'prev' and current_page > 1:
        current_page -= 1


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
                while True:
                    os.system('clear')
                    if role == '新闻编辑':
                        pass
                    elif role == '管理员':
                        print(Fore.LIGHTBLUE_EX, '\n\t1.新闻管理')
                        print(Fore.LIGHTBLUE_EX, '\n\t2.用户管理')
                        print(Fore.LIGHTRED_EX, '\n\tback.退出登录')
                        print(Fore.LIGHTRED_EX, '\n\texit.退出系统')
                        print(Style.RESET_ALL)
                        choice = input('\n\t输入操作编号:')
                        if choice == '1':
                            while True:
                                os.system('clear')
                                print(Fore.LIGHTBLUE_EX, '\n\t1.审批新闻')
                                print(Fore.LIGHTBLUE_EX, '\n\t2.删除新闻')
                                print(Fore.LIGHTRED_EX, '\n\tback.返回上一层')
                                print(Style.RESET_ALL)
                                opt = input('\n\t输入操作编号:')
                                if opt == '1':
                                    current_page = 1
                                    while True:
                                        os.system('clear')
                                        count_page = __news_service.search_unreview_page_count()
                                        result = __news_service.search_unreview_list(current_page)
                                        break_flag = False

                                        if break_flag:
                                            break
                                        if 1 <= int(opt) <= 10:
                                            update_id = result[int(opt) - 1][0]
                                            __news_service.update_unreview_count(update_id)
                                elif opt == '2':
                                    current_page = 1
                                    while True:
                                        os.system('clear')
                                        count_page = __news_service.search_count_page()
                                        result = __news_service.search_list(current_page)
                                        break_flag = False
                                        show_list(result, current_page)
                                        if break_flag:
                                            break
                                        if 1 <= int(opt) <= 10:
                                            delete_id = result[int(opt) - 1][0]
                                            __news_service.delete_new_by_id(delete_id)
                                elif opt == 'back':
                                    break
                        elif choice == '2':
                            while True:
                                os.system('clear')
                                print(Fore.LIGHTBLUE_EX, '\n\t1.添加用户')
                                print(Fore.LIGHTBLUE_EX, '\n\t2.修改用户')
                                print(Fore.LIGHTBLUE_EX, '\n\t3.删除用户')
                                print(Fore.LIGHTRED_EX, '\n\tback.返回上一层')
                                print(Style.RESET_ALL)
                                opt = input('\n\t输入操作编号:')
                                if opt == '1':
                                    os.system('clear')
                                    username = input('\n\t请输入用户名:')
                                    password = getpass('\n\t请输入密码:')
                                    password2 = getpass('\n\t请再次输入密码:')
                                    if password != password2:
                                        print('\n\t两次输入的密码不一致,3秒后自动返回')
                                        time.sleep(3)
                                        continue
                                    email = input('\n\t请输入邮箱:')
                                    result = __role_srvice.search_list()
                                    for index, value in enumerate(result):
                                        print(Fore.LIGHTBLUE_EX,
                                              '\n\t%d\t%s' % (index + 1, value[1]))
                                    print(Style.RESET_ALL)
                                    choice_role = input('\n\t请输入角色编号:')
                                    role_id = result[int(choice_role) - 1][0]
                                    __user_service.user_insert(username, password, email, role_id)
                                    print('\n\t保存成功,3秒后自动返回')
                                    time.sleep(3)
                                if opt == '2':
                                    current_page = 1
                                    while True:
                                        os.system('clear')
                                        count_page = __user_service.search_page_count()
                                        result = __user_service.search_list(current_page)
                                        for index, value in enumerate(result):
                                            print(Fore.LIGHTBLUE_EX,
                                                  '\n\t%d\t%s' % (index + 1, value[1]))
                                        print(Fore.LIGHTBLUE_EX, '\n\t========================================')
                                        print(Fore.LIGHTBLUE_EX, '\n\t当前在第%d页 共%d页' % (current_page, count_page))
                                        print(Fore.LIGHTBLUE_EX, '\n\t========================================')
                                        print(Fore.LIGHTRED_EX, '\n\tback.返回上一层')
                                        print(Fore.LIGHTRED_EX, '\n\tprev.上一页')
                                        print(Fore.LIGHTRED_EX, '\n\tnext.下一页')
                                        print(Style.RESET_ALL)
                                        opt = input('\n\t输入操作编号:')
                                        if opt == 'back':
                                            break
                                        elif opt == 'next' and current_page < count_page:
                                            current_page += 1
                                        elif opt == 'prev' and current_page > 1:
                                            current_page -= 1
                                        elif 1 <= int(opt) <= 10:
                                            update_id = result[int(opt) - 1][0]
                                            os.system('clear')
                                            username = input('\n\t请输入用户名:')
                                            password = getpass('\n\t请输入密码:')
                                            password2 = getpass('\n\t请再次输入密码:')
                                            if password != password2:
                                                print('\n\t两次输入的密码不一致,3秒后自动返回')
                                                print(Style.RESET_ALL)
                                                time.sleep(3)
                                                continue
                                            email = input('\n\t请输入邮箱:')
                                            role_result = __role_srvice.search_list()
                                            for index, value in enumerate(role_result):
                                                print(Fore.LIGHTBLUE_EX,
                                                      '\n\t%d\t%s' % (index + 1, value[1]))
                                            print(Style.RESET_ALL)
                                            choice_role = input('\n\t请输入角色编号:')
                                            role_id = role_result[int(choice_role) - 1][0]
                                            last_choice = input('\n\t是否保存(Y/N):')
                                            if last_choice == 'Y':
                                                __user_service.user_update(update_id, username, password, email,
                                                                           role_id)
                                                print('\n\t保存成功,3秒后自动返回')
                                                time.sleep(3)
                                            elif last_choice == 'N':
                                                print('\n\t3秒后自动返回')
                                                time.sleep(3)
                                if opt == '3':
                                    current_page = 1
                                    while True:
                                        os.system('clear')
                                        count_page = __user_service.search_page_count()
                                        result = __user_service.search_list(current_page)
                                        for index, value in enumerate(result):
                                            print(Fore.LIGHTBLUE_EX,
                                                  '\n\t%d\t%s' % (index + 1, value[1]))
                                        print(Fore.LIGHTBLUE_EX, '\n\t========================================')
                                        print(Fore.LIGHTBLUE_EX, '\n\t当前在第%d页 共%d页' % (current_page, count_page))
                                        print(Fore.LIGHTBLUE_EX, '\n\t========================================')
                                        print(Fore.LIGHTRED_EX, '\n\tback.返回上一层')
                                        print(Fore.LIGHTRED_EX, '\n\tprev.上一页')
                                        print(Fore.LIGHTRED_EX, '\n\tnext.下一页')
                                        print(Style.RESET_ALL)
                                        opt = input('\n\t输入操作编号:')
                                        if opt == 'back':
                                            break
                                        elif opt == 'next' and current_page < count_page:
                                            current_page += 1
                                        elif opt == 'prev' and current_page > 1:
                                            current_page -= 1
                                        elif 1 <= int(opt) <= 10:
                                            delete_id = result[int(opt) - 1][0]
                                            __user_service.user_delete(delete_id)
                                            print('\n\t删除成功,3秒后自动返回')
                                if opt == 'back':
                                    break
                        elif choice == 'back':
                            break
                        elif choice == 'exit':
                            sys.exit(0)
            else:
                print(Fore.LIGHTYELLOW_EX, '\n\t登录失败(稍后自动返回)')
                time.sleep(2)

        elif opt == '2':
            sys.exit(0)
