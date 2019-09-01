#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 类装饰器.py
# @Author: smx
# @Date  : 2019/8/14
# @Desc  :

class A(object):
    def __init__(self, func):
        print('定义初始化函数')
        print('func name is %s' % func.__name__)
        self.__func = func

    def __call__(self):
        print('call 方法作为装饰器中的功能')
        self.__func()
        print('增加的功能2')


@A
def B():
    print('这个是B是原函数')
# 这里输入是因为装饰器在定义的时候调用，但是原本的b函数没有调用


# A(B) # 这里也是装饰器
# 如果不看装饰器的作用的话,这里的 A(B)和上面的 @A相等作用相同,但是这里的作用就是是装饰器了,就只是简单的函数调用了,所以就不会调用call方法了

# 调用装饰器的时候是调用call函数，然后调用被装饰的函数
B()
# 整体的发生顺序
# 1. 装饰器的函数定义
# 2. 装饰器的call函数
# 3. 装饰器调用被装饰的函数