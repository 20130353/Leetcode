#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 紧急疏散.py
# @Author: smx
# @Date  : 2019/8/17
# @Desc  :
# 这道题本质就是多叉树的层次遍历
# 重点是用邻接矩阵形成多叉树

# 这里理解错误，不是层次遍历，因为除了根节点之外的节点都需要等待
# 所以改成第二层节点的最多子节点数目就是影响时间的关键因素
# 其实我自己的想法是对的，但是没有进一步找到数字之间的规律！

# 存在的问题是：超内存 -->
# 用dict保存节点 +  不用找第二层的节点，直接一起算. 这样就对了！

#
# 收获：
# 1. 计算第二层的节点，不需要先找到第二层节点，应该可以直接从当前的根节点的孩子节点开始
# 2. 不要用mat存储节点，用dict存储更省内存！

def solution(mat, n):
    vis = [0] * n
    max_num = 0
    vis[0] = 1
    for u in mat[0]:
        vis[u] = 1
        queue = [u]
        num = 0
        while len(queue) != 0:
            num += 1
            v = queue.pop()
            for i in mat[v]:
                if vis[i] == 0:
                    vis[i] = 1
                    queue.append(i)
        max_num = max(num, max_num)
    return max_num


if __name__ == '__main__':
    n = int(input().strip())
    mat = {}
    for i in range(n):
        mat[i] = []
    for _ in range(n - 1):
        i, j = map(int, input().strip().split(' '))
        mat[i - 1].append(j - 1)
        mat[j - 1].append(i - 1)

    ans = solution(mat, n)
    print(ans)
