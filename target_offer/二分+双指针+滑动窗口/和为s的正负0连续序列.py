# -*- coding: utf-8 -*-
# author: sunmengxin
# time: 18-11-25
# file: 和为s的连续正整数数列
# description:

# 这道题和树的最大路径和一样
def solution(arr, n, target):
    if sum(arr) == target:
        return n

    sum_map = {0: 0}
    cur_sum, max_leng = 0, -1
    # max_start = -1
    for i in range(1, n + 1):
        cur_sum += arr[i - 1]
        if cur_sum not in sum_map.keys():
            sum_map[cur_sum] = i
        if (cur_sum - target) in sum_map and (i - sum_map[cur_sum - target]) > max_leng:
            max_leng = i - sum_map[cur_sum - target]
            # max_start = sum_map[cur_sum - target]
    return max_leng


if __name__ == '__main__':
    n, k = map(int, input().strip().split(' '))
    arr = list(map(int, input().strip().split(' ')))
    ans = solution(arr, n, k)
    print(ans)
