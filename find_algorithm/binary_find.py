# -*- coding: utf-8 -*-
# Author: sunmengxin
# time: 10/8/18
# file: binary_find.py
# description:

def binary_find(data, v):
    # 没有重复元素
    low = 0
    high = len(data) - 1
    #  这里如果是等于会出现死循环
    while (low < high):
        mid = (low + high) // 2  # 这里用整除操作符号
        if data[mid] == v:
            return mid
        if data[mid] < v:
            low = mid + 1
        else:
            high = mid - 1  # 二分查找一定要排除中间的mid
    return -1


def solution(arr, target):
    if arr.__len__() <= 0:
        return -1

    # 如果有重复元素，返回第一次出现的位置
    low, high = 0, arr.__len__() - 1
    while low < high:
        mid = low + (high - low) // 2
        if arr[mid] < target:
            low = mid + 1
        else:
            high = mid
    return low if arr[low] == target else -1


# 本质问题是：看mid是answer区间向左/右移动
def solution(arr, target):
    if arr.__len__() <= 0:
        return -1

    # 如果有重复元素，返回最后一次出现的位置
    low, high = 0, arr.__len__() - 1
    while low < high:
        mid = low + (high - low + 1) >> 2
        if arr[mid] <= target:
            low = mid
        else:
            high = mid - 1
    return low if arr[low] == target else -1


if __name__ == '__main__':
    # arr = []
    # arr = [1]
    arr = [1, 2, 3, 4, 4, 4, 4, 5, 7, 9, 20]
    ans = solution(arr, 4)
    print(ans)

