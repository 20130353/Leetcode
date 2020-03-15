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

'''

# 用切分的方式比用数组下标的方式容易实现多了！
def find_k(arr, n, k):
    def partition(arr, low, high):
        key = arr[low]
        i, j = low, high - 1
        while i < j:
            while i < j and arr[j] >= key:
                j -= 1
            if i < j:
                arr[i] = arr[j]
            while i < j and arr[i] <= key:
                i += 1
            if i < j:
                arr[j] = arr[i]
        arr[i] = key
        return i

    def quick_sort(arr, low, high, k):
        mid = partition(arr, low, high)
        if mid == k - 1:
            return arr[mid]
        elif mid > k - 1:
            return quick_sort(arr, low, mid, k)
        else:
            return quick_sort(arr, mid + 1, high, k)
    return quick_sort(arr, 0, n, k)


# def find_k(arr, k):
#     i, j = 0, len(arr) - 1
#     key = arr[i]
#     while i < j:
#         while i < j and arr[j] >= key:
#             j -= 1
#         if i < j:
#             arr[i] = arr[j]
#         while i < j and arr[i] < key:
#             i += 1
#         if i < j:
#             arr[j] = arr[i]
#     arr[j] = key
#     if i == k - 1:
#         return arr[i]
#     elif i < k:
#         return find_k(arr[i + 1:], k - i - 1)
#     else:
#         return find_k(arr[:i], k)
#

if __name__ == '__main__':
    string = input().strip()
    # string = '[0,0,0,0,2,0,1]'
    arr = list(map(int, string.replace('[', '').replace(']', '').split(',')))
    ans = find_k(arr, len(arr), len(arr) - 2)
    print(ans)
