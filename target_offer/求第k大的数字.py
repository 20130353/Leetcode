# -*- coding: utf-8 -*-
# Author: sunmengxin
# time: 10/15/18
# file: 求第k大的数字.py
# description:

'''
给定一个数组,求数组的第k大数字
# 有六种解法:
解法1. 排序,然后数第k个
解法2. 冒泡排序,选择排序,插入排序等算法到第k个就结束
解法3. 海量数据可以先随机选择k个,然后依次把剩下的数据和他们相比,如果比他们小,就更新k个数据
解法4. 用大根堆和小根堆实现
解法5. 快速排序,分成两部分,和大根堆和小根堆的想法差不多,但是每次可以淘汰一般的数据
解法6. 五划分中项法

这里我们实现解法5.
'''

def get_k(data,k):

    low = 0
    high = len(data)-1
    key = data[low]

    while(low < high):
        while(low < high and data[high] > key):
            high -= 1
        if (low < high):
            data[low] = data[high]
        while(low < high and data[low] < key):
            low += 1
        if (low < high):
            data[high] = data[low]
    data[low] = key
    if low == k:
        return data[low]
    else:
        if low < k:
            return get_k(data[low:],k-low-1)
        else:
            return get_k(data[:low],k)

if __name__ == '__main__':
    data = [3,4,6,1,8,2]
    res = get_k(data,3)
    print(res)