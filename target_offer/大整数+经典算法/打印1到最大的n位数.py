# -*- coding: utf-8 -*-
# Author: sunmengxin
# time: 10/11/18
# file: 打印1到最大的n位数.py
# description:

'''
 打印从1到n的最大n位数
 比如n=3，打印 1 2 3 .... 999
 可能n很大，变成大数问题
'''

import numpy as np

def add_string(string):
    inx = len(string)-1
    tens = 1
    while(tens and inx>=0):
        add_res = np.int(string[inx]) + tens
        unit = np.int(add_res%10)
        string = string[:inx] + str(unit) + string[inx+1:]
        tens = np.int(add_res/10)
        inx -= 1
    if inx < 0 and tens != 0:
        flag = True
    else:
        flag = False
    return flag,string

def print_string(string):
    flag = False
    for inx in range(0,len(string)):
        if string[inx] != '0' or flag == True:
            flag = True
            if inx != len(string)-1:
                print(string[inx],end='')
            else:
                print(string[inx])
    return

# 使用字符串模拟数字和数字加法
# 每次数字加一
def string_solution(n):
    if n <= 0:
        return
    # from high bit to low bit
    string = '0'
    string_max = '9'
    for _ in range(n-1):
        string += '0'
        string_max += '9'

    while(True):
        flag,string = add_string(string)
        if flag == True:
            break
        else:
            print_string(string)
            if string == string_max:
                break

def print_array(data):
    flag = False
    for inx in range(0,len(data)):
        if data[inx] != 0 or flag == True:
            flag = True
            if inx != len(data)-1:
                print(np.int(data[inx]),end='')
            else:
                print(np.int(data[inx]))
    return

# 使用全排列来输出
def string_permutation(array,length,index):
    if length <= 0 or len(array) <= 0:
        return
    if index == length:
        print_array(array)
        return
    for num in range(0,10):
        array[index] = num
        string_permutation(array,length,index+1)

    return

if __name__ == '__main__':

    # 使用字符串模拟数字
    # print('n==0')
    # string_solution(0)
    #
    # print('n==1')
    # string_solution(1)

    # print('n==3')
    # string_solution(3)

    # print('n==100')
    # string_solution(100)


    print('n==0')
    n=0
    array = np.zeros(n)
    string_permutation(array,n,0)

    print('n==3')
    n=3
    array = np.zeros(n)
    string_permutation(array,n,0)