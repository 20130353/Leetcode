# -*- coding: utf-8 -*-
# author: sunmengxin
# time: 18-11-25
# file: 和为s的连续正整数数列
# description:

# 您的代码已保存
# 运行超时:您的程序未能在规定时间内运行结束，请检查是否循环有错或算法复杂度过大。
# case通过率为20.00%

# 这里本质就是找>=sum-k的最大位置，所以可以用二分优化
# sum和保存的是某位置前面的累加和的最大值

# 您的代码已保存
# 答案错误:您提交的程序没有通过所有的测试用例
# case通过率为60.00%

def binary_search(arr, n, target):
    # 找到>target的最大位置
    low, high = 0, n - 1
    ans = -1
    while low < high:
        mid = low + (high - low) // 2
        if arr[mid] < target:
            low = mid + 1
        else:
            high = mid
            ans = mid
    return ans

# 时间复杂度O(NlogN)，空间复杂度O(N)。
def solution(arr, n, target):
    if sum(arr) == target:
        return n
    sum_arr, cur_sum = [arr[0]], 0
    max_leng = -1
    for i in range(1, n):
        cur_sum += arr[i]
        sum_arr.append(max(cur_sum, sum_arr[-1]))

    # print(sum_arr)
    # 在每一个位置找到>=sum-k的最大位置（二分法）
    # max_start = -1
    cur_sum = 0
    for i in range(n):
        cur_sum += arr[i]
        pos = binary_search(sum_arr, len(sum_arr), cur_sum - target)
        if pos != -1 and i - pos + 1 > max_leng:
            max_leng = i - pos + 1
            # max_start = pos
    return max_leng

# #python3.5
# def maxLen2(arr, k):
#     if arr == None or len(arr) == 0:
#         return 0
#     help = [0 for i in range(len(arr))]   #以i位置开头能达到的最小累加和
#     help[-1] = arr[-1]
#     map = {}   #以位置i开头的最小累加和数组的最右位置
#     map[len(arr)-1] = len(arr) - 1
#     for i in range(len(arr)-2, -1, -1):
#         if help[i+1] <= 0:
#             help[i] = help[i+1] + arr[i]
#             map[i] = map[i+1]
#         else:
#             help[i] = arr[i]
#             map[i] = i
#     res = 0   #全局变量记录最大子数组长度
#     end = 0   #子数组右边界的下一个位置
#     sum = 0   #子数组累加和
#     for i in range(len(arr)):
#         #计算以i位置开头满足条件的最大子数组
#         while end < len(arr) and sum + help[end] <= k:
#             sum += help[end]
#             end = map[end] + 1
#         #更新最大子数组长度
#         res = max(res, end - i)
#         #子数组左边界向右移动一位
#         sum -= arr[i] if end > i else 0
#         #更新end
#         end = end if end > i else i + 1
#     return res



if __name__ == '__main__':
    n, k = map(int, input().strip().split(' '))
    arr = list(map(int, input().strip().split(' ')))
    ans = solution(arr, n, k)
    print(ans)
