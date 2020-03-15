#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 地鼠逃跑计划.py
# @Author: smx
# @Date  : 2020/2/16
# @Desc  :

# 这道题有两个关键的地方：
# 1. 从边界点到x，y点
# 2. 减少for，改进超时问题

# class Solution():
#     def find_way(self, m, n, x, y, k):
#         # 超时！-->改成DFS
#         # 用队列的方式比栈的时间开销更大
#         dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]
#         queue = [(x, y)]
#         ans = 0
#         while k and queue:
#             length = len(queue)
#             while length:
#                 i, j = queue.pop(0)
#                 length -= 1
#                 if abs(i) > k and abs(j) > k and abs(m - i) > k and abs(n - j) > k:
#                     continue
#                 for l in range(4):
#                     new_i = i + dir[l][0]
#                     new_j = j + dir[l][1]
#                     if new_i >= 0 and new_j >= 0 and new_i < m and new_j < n:
#                         queue.append((new_i, new_j))
#                     else:
#                         ans += 1
#             k -= 1
#         return ans

# for 很浪费时间！
# 存在的问题是可能出现同一个地点到过两次
def DFS(m, n, x, y, k, ans):
    if k < 0:
        return

    if x < 0 or y < 0 or x >= m or y >= n:
        ans[0] += 1
        return
    DFS(m, n, x - 1, y, k - 1, ans)
    DFS(m, n, x + 1, y, k - 1, ans)
    DFS(m, n, x, y - 1, k - 1, ans)
    DFS(m, n, x, y + 1, k - 1, ans)


if __name__ == '__main__':
    m = int(input().strip())
    n = int(input().strip())
    x = int(input().strip())
    y = int(input().strip())
    k = int(input().strip())
    ans = [0]
    DFS(m, n, x, y, k, ans)
    print(ans[0])
