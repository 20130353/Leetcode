#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 建物流中转站.py
# @Author: smx
# @Date  : 2019/8/13
# @Desc  :
#
# Shopee物流会有很多个中转站。在选址的过程中，会选择离用户最近的地方建一个物流中转站。
#
# 假设给你一个二维平面网格，每个格子是房子则为1，或者是空地则为0。找到一个空地修建一个物流中转站，使得这个物流中转站到所有的房子的距离之和最小。 能修建，则返回最小的距离和。如果无法修建，则返回 -1。
#
#
# 若范围限制在100*100以内的网格，如何计算出最小的距离和？
#
# 当平面网格非常大的情况下，如何避免不必要的计算？

# 这样做超时，只能过66.7的case
def solution1(mat):
    loc0 = []
    loc1 = []
    for i in range(n):
        for j in range(n):
            if mat[i][j] == '1':
                loc1.append((i, j))
            else:
                loc0.append((i, j))

    if len(loc0) == 0:
        print(-1)
    else:
        min_dis = float('inf')
        min_loc = None
        for each0 in loc0:
            dis = 0
            for each1 in loc1:
                if dis > min_dis:
                    break
                dis += abs(each0[0] - each1[0]) + abs(each0[1] - each1[1])
            if dis < min_dis:
                min_dis = dis
                min_loc = each0

    print('solution1')
    print(min_loc)
    print(min_dis)
    return min_dis

#
# 存在的问题：超时，不能直接计算所有空地到建筑物的距离 -》 找中心
# 存在的问题：中心不是矩阵的中心 -》 是建筑物的中心
# 存在的问题：此时的坐标很可能是小数，但不影响，我们接下来只要找到距离这个坐标最近的空地
# def solution(mat, n):
#     loc0 = []
#     loc1 = []
#     mean_loc = None
#     for i in range(n):
#         for j in range(n):
#             if mat[i][j] == '1':
#                 loc1.append((i, j))
#             else:
#                 loc0.append((i, j))
#                 if mean_loc is None:
#                     mean_loc = (i, j, abs(i - n) + abs(j - n))
#                 else:
#                     if abs(i - n // 2) + abs(j - n // 2) < mean_loc[2]:
#                         mean_loc = (i, j, abs(i - n // 2) + abs(j - n // 2))
#
#     if len(loc0) == 0:
#         print(-1)
#     else:
#         min_dis = 0
#         for each in loc1:
#             min_dis += abs(mean_loc[0] - each[0]) + abs(mean_loc[1] - each[1])
#         print(min_dis)
#         print(mean_loc)
#         min_loc = None
#         for each0 in loc0:
#             dis = 0
#             for each1 in loc1:
#                 if dis > min_dis:
#                     break
#                 dis += abs(each0[0] - each1[0]) + abs(each0[1] - each1[1])
#             if dis < min_dis:
#                 min_dis = dis
#                 min_loc = (i, j)
#     print(min_loc)
#     print(min_dis)
#     return min_dis


#  模仿kmeans算法，求中心
def solution(mat, n):
    loc0 = []
    loc1 = []
    sum_i, sum_j, count = 0, 0, 0
    for i in range(n):
        for j in range(n):
            if mat[i][j] == '1':
                loc1.append((i, j))
                sum_i += i
                sum_j += j
                count += 1
            else:
                loc0.append((i, j))
    if len(loc0) == 0:
        return -1
    else:
        mean_loc = (sum_i / count, sum_j / count)
        true_loc = None
        for each in loc0:
            if true_loc is None:
                true_loc = each
            elif abs(true_loc[0] - mean_loc[0]) + abs(true_loc[1] - mean_loc[1]) > \
                    abs(each[0] - mean_loc[0]) + abs(each[1] - mean_loc[1]):
                true_loc = each
        min_dis = 0
        for each in loc1:
            min_dis += abs(true_loc[0] - each[0]) + abs(true_loc[1] - each[1])
        return min_dis


if __name__ == '__main__':
    n = int(input().strip())
    mat = []
    for _ in range(n):
        mat.append(list(input().strip().split(' ')))
    ans = solution(mat, n)
    print(ans)
