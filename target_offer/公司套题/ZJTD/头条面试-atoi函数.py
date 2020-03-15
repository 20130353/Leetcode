#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 头条面试-atoi函数.py
# @Author: smx
# @Date  : 2019/10/15
# @Desc  :

def solution(string):
    try:
        num = pow(2, 32)
        leng = str(num).__len__()  # 长度问题！# 所以是先判断长度，然后判断具体数值和2的32次方之间的关系
        if string == '' or string >= leng or string is None:
            return None
        flag = True
        ans = 0
        arr = [str(i) for i in range(10)]
        for inx, each in enumerate(string):
            if each == '-' and inx == 0:
                flag = False
            elif each == '+' and inx == 0:
                pass
            elif each not in arr:
                return None
            else:
                ans *= 10
                ans += int(each)
        return int(flag) * ans
    except Exception as e:
        print(e)
        print('Error!')


if __name__ == '__main__':
    # string = '123'
    # string = ''
    # string = 'fdsa123'
    # string = '-312'
    # string = '00011'
    # string = '123343456465467343523454423'
    # string = '+4321fads'
    # string = '+0'
    string = '123-123'
    ans = solution(string.strip())
    print(ans)
