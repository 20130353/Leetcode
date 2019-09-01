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

# def find_k(arr, low, high, k):
#     if low >= high:
#         return arr[low]
#     i, j = low, high
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
#     print('-------------------------')
#     print(arr)
#     print(low, high, k)
#     print(key, i, arr[j])
#     if i == k:
#         return arr[i]
#     elif i < k:
#         return find_k(arr, i + 1, high, k - i - 1)
#     else:
#         return find_k(arr, low, i - 1, k)
# 这种方法错误是因为每次用i来和k比较出现重复减少数据的情况， 所以只能用分割数字的方式

# 实现过程中遇到的难点是：
# 1. 快速排序实现有问题， 最后将key赋值回去的时候使用i，原来以为使用i是不对的， 改成使用j，但是后来又发现使用i和使用j是一样的， 以为最后i=就，所以使用i和j都行
# 2. 判断是否当前的mid位置的元素是不是第k个元素，应该用k-1,因为下表索引从0开始
# 3. 下一次迭代的时候把数组所有元素放入，因为会多次k-i
def find_k(arr, k):
    i, j = 0, len(arr) - 1
    key = arr[i]
    while i < j:
        while i < j and arr[j] >= key:
            j -= 1
        if i < j:
            arr[i] = arr[j]
        while i < j and arr[i] < key:
            i += 1
        if i < j:
            arr[j] = arr[i]
    arr[j] = key
    if i == k - 1:
        return arr[i]
    elif i < k:
        return find_k(arr[i + 1:], k - i - 1)
    else:
        return find_k(arr[:i], k)


if __name__ == '__main__':
    import sys

    for line in sys.stdin:
        arr = list(map(int, line.strip().replace('[', '').replace(']', '').split(',')))
        ans = find_k(arr, len(arr) - 2)
        print(ans)
