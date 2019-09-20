#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 和小于等于K的子数组个数.py
# @Author: smx
# @Date  : 2019/9/15
# @Desc  :


from functools import reduce


def solution(arr, n, k):
    def dfs(arr, n, k, vis, cur_index, cur_pos, cur_sum, target_leng, ans):
        if cur_pos == target_leng:
            if cur_sum < k:
                ans[0] += 1
                # temp = ''
                # for i in range(n):
                #     if vis[i] == 1:
                #         temp += ' ' + str(arr[i])
                # print(temp)
            return

        if cur_index >= n or cur_sum > k:
            return

        for i in range(cur_index + 1, n):
            if vis[i] == 0 and cur_sum + arr[i] < k:
                vis[i] = 1
                dfs(arr, n, k, vis, i, cur_pos + 1, cur_sum + arr[i], target_leng, ans)
                vis[i] = 0
        return

    if min(arr) >= k:
        return 0

    if sum(arr) < k:
        fenzi = reduce(lambda x, y: x * y, range(1, n + 1))
        fenmu = reduce(lambda x, y: x * y, range(1, 3 + 1)) * reduce(lambda x, y: x * y, range(1, (n - 3) + 1))
        return round(fenzi / fenmu, 0)

    ans = [0]
    vis = [0] * n
    dfs(arr, n, k, vis, -1, 0, 0, 3, ans)
    return ans[0]


if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    k = int(input().strip())
    ans = solution(arr, n, k)
    print('%d' % ans)

# 10
# 1 2 3 4 5 6 7 8 9 10
# 5

# 10
# 5 5 5 5 5 5 5 5 5 5
# 4

# 1
# 3
# 10
