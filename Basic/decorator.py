#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/11/8 0:21
# @Author  : Haorui Guo
# @File    : decorator.py
import time
import functools


def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        func(*args, **kwargs)
        t2 = time.time()
        print('Function {} takes {} to execute'.format(func.__name__, t2 - t1))

    return wrapper


# func = timer(func)
@timer
def func():
    time.sleep(1)


if __name__ == '__main__':
    func()
    print(func.__name__)
