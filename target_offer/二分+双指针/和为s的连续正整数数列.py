# -*- coding: utf-8 -*-
# author: sunmengxin
# time: 18-11-25
# file: 和为s的连续正整数数列
# description:
# 是因为有正数所以可以省略
def solution(arr, n, target):
    if sum(arr) < target or target <= 0:
        return -1

    if sum(arr) == target:
        return n

    i, j = 0, 0
    cur_sum = arr[0]
    max_leng, max_start = -1, -1
    while i < n and j < n:
        if cur_sum >= target:
            if cur_sum == target and j - i + 1 > max_leng:
                max_start = i
                max_leng = max(max_leng, j - i + 1)
            cur_sum -= arr[i]
            i += 1
        else:
            j += 1
            if j < n:
                cur_sum += arr[j]
    # print(max_start, max_leng, arr[max_start:max_start + max_leng])
    return max_leng


if __name__ == '__main__':
    n, k = map(int, input().strip().split(' '))
    arr = list(map(int, input().strip().split(' ')))
    ans = solution(arr, n, k)
    print(ans)
