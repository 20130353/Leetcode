# -*- coding: utf-8 -*-
# Author: sunmengxin
# time: 10/20/18
# file: 数组中的逆序对.py
# description:
'''
    两个数字如果前面的数字大于大于后面的数字就称为逆序对,求给定数组中的逆序对个数
    两种解法:
    1. 两个for 循环遍历
    2. 利用归并思想
'''

def inverse_pair(data):
    if data == None or len(data) == 0:
        return data,0
    if len(data) == 1:
        return data,0

    low = 0
    high = len(data)
    mid = (low+high)//2
    left,cnt1 = inverse_pair(data[:mid])
    right,cnt2 = inverse_pair(data[mid:])
    data,count = merge(left,right)
    return data,count+cnt1+cnt2

def merge(left,right):
    new = []
    count = 0
    while len(left) and len(right):
        if left[-1] > right[-1]:
            count += len(right)
            new.insert(0,left[-1])
            del left[-1]
        elif left[-1] < right[-1]:
            new.insert(0,right[-1])
            del right[-1]
    if len(left):
        while(len(left)):
            new.insert(0,left[-1])
            del left[-1]
    if len(right):
        while (len(right)):
            new.insert(0, right[-1])
            del right[-1]
    return new,count

if __name__ == '__main__':
    data = [2,1]
    res_data,res_count = inverse_pair(data)
    print(res_count)


