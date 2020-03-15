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

    left = 0
    win = 0
    max_length = -0xfffff
    # 核心是右边一直不断加入，左边是看情况收缩
    for right in range(n):
        win += arr[right]
        while left < right and win >= target:
            if win == target:
                max_length = max(max_length, right - left + 1)
            win -= arr[left]
            left += 1
    return max_length




if __name__ == '__main__':
    n, k = map(int, input().strip().split(' '))
    arr = list(map(int, input().strip().split(' ')))
    ans = solution(arr, n, k)
    print(ans)
