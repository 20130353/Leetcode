#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 不同的二叉搜索树.py
# @Author: smx
# @Date  : 2019/8/31
# @Desc  :

# 当n=0的时候，一颗空树
#
# 当n=1的时候，等于其左子树的种类数目*右子树的种类数目，因为左子树的元素数目为0，右子树的元素数目也是0，所以结果是1*1=1，
#
# 当n=2的时候，等于以1为根的树的数目+以2为根的树的数目，当以1为根时，其左子树的元素数目为0，因为不会有数比1小，其右子树的元素数目为1，因为比1大的只有2一个数，因此是不是又可以转化为左子树的元素为0的情况和右子树的元素为1的情况，是不是就等于1*1=1，同理以2为根的树的数目计算结果也是1*1=1，和就是2


def solution(n):
    dp = [1, 1, 2] + [0] * n
    for i in range(3, n + 1):
        for j in range(1, i + 1):
            dp[i] += dp[j - 1] * dp[i - j]
    return dp[n]


if __name__ == '__main__':
    n = int(input().strip())
    ans = solution(n)
    print(ans)
