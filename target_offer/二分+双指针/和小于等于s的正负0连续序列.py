# -*- coding: utf-8 -*-
# author: sunmengxin
# time: 18-11-25
# file: 和为s的连续正整数数列
# description:

# 直接map保存
# 运行超时:您的程序未能在规定时间内运行结束，请检查是否循环有错或算法复杂度过大。
# case通过率为20.00%

# 排序+二分优化
# def binary_search(sum_dict, target):
#     arr = sorted(sum_dict.keys())
#     low, high = 0, len(arr) - 1
#
#     pos = float('inf')
#     # 这里找到每一次等于target的位置，记录对应的最小i
#     while low < high:
#         mid = low + (high - low) // 2
#         if arr[mid] < target:
#             low = mid + 1
#         else:
#             high = mid
#         if arr[high] >= target:
#             pos = min(sum_dict[arr[high]], pos)
#     return pos
#
#
# def solution(arr, n, target):
#     # 主要是用二分查找找到最大的和的位置
#     sum_dict = {0: 0}
#
#     sum_i = 0
#     max_start, max_leng = -1, 0
#     for i in range(n):
#         sum_i += arr[i]
#         if sum_i not in sum_dict:
#             sum_dict[sum_i] = i + 1
#
#         pos = binary_search(sum_dict, sum_i - target)
#         if pos != float('inf'):
#             if i - pos + 1 > max_leng:
#                 max_leng = i - pos + 1
#                 max_start = pos
#     return max_leng, max_start
#

# 累加和+二分
# 答案错误:您提交的程序没有通过所有的测试用例
# case通过率为60.00%

# 3 2
# 1 1 1
# 错误个数

# 10 8
# 10 12 20 30 29 1 0 8 30 1
# 还是有错误！

# 运行超时:您的程序未能在规定时间内运行结束，请检查是否循环有错或算法复杂度过大。
# case通过率为70.00%

# 加了sum[0]=0 和 二分查找的时候 只找i以前的！
# --》AC

# 之前累加和包不包括pos这个点需要写很多，如果假如0就很清楚！

def binary_search(arr, n, target):
    low, high = 0, n
    ans = -1
    while low < high:
        mid = low + (high - low) // 2
        if arr[mid] < target:
            low = mid + 1
        else:
            high = mid
            ans = mid
    return ans


def solution(arr, n, target):
    if sum(arr) <= target:
        return n

    sum_arr, cur_sum = [0], 0
    max_leng = 0
    for i in range(n):
        cur_sum += arr[i]
        if i != 0:
            sum_arr.append(max(cur_sum, sum_arr[-1]))
        else:
            sum_arr.append(cur_sum)

        pos = binary_search(sum_arr, i, cur_sum - target)
        if pos != -1 and i - pos + 1 > max_leng:
            max_leng = i - pos + 1
    return max_leng


if __name__ == '__main__':
    n, k = map(int, input().strip().split(' '))
    arr = list(map(int, input().strip().split(' ')))
    ans = solution(arr, n, k)
    print(ans)
