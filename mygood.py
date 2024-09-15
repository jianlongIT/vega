# -*- coding: utf-8 -*-
# Auther : jianlong
import random

if __name__ == '__main__':
    my_list = []
    while len(my_list) < 6:
        num = random.randint(1, 33)
        if num not in my_list:
            my_list.append(num)
    my_list.sort()
    last_num = random.randint(1, 16)

    print(*my_list, last_num)
