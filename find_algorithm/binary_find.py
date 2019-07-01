# -*- coding: utf-8 -*-
# Author: sunmengxin
# time: 10/8/18
# file: binary_find.py
# description:

def binary_find(data,v):

    low = 0
    high = len(data) - 1
#  这里如果是等于会出现死循环
    while(low < high):
        mid = (low+high)//2 # 这里用整除操作符号
        if data[mid] == v:
            return mid
        if data[mid] < v:
            low = mid + 1
        else:
            high = mid - 1 # 二分查找一定要排除中间的mid
    return -1


if __name__ == '__main__':
    data = [1,2,3,4,5,6,7,8,8,8,8,9]
    data = sorted(data)
    inx = binary_find(data,8)
    print(inx)

