#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 外卖满减.py
# @Author: smx
# @Date  : 2019/8/19
# @Desc  :


# 你打开了美了么外卖，选择了一家店，你手里有一张满X元减10元的券，店里总共有n种菜，第i种菜一份需要A_i元，
# 因为你不想吃太多份同一种菜，所以每种菜你最多只能点一份，现在问你最少需要选择多少元的商品才能使用这张券。


# 存在的问题：找不到递归方程，找不到最低价的表示方式 -》 注意观察什么变量是变化的，分析变量可变的情况！

# 注意和01背包区别：和之前状态比较和自己状态比较

def solution(n, x, arr):
    max_value = sum(arr)
    if max_value == x:
        return x
    dp = [max_value] * x
    for i in range(n):
        for j in range(x - 1, -1, -1):
            if j >= arr[i]:
                dp[j] = min(dp[j], dp[j - arr[i]] + arr[i])
                # 如果dp[i-a[i]]+a[i] 不能满足最低价格呢？所以需要保证初始的购买物价一定满足最小购物券价格或者是中间的价格是满足最低价的最小价格！
            else:
                dp[j] = min(dp[j], arr[i])  # 当前物品的价格比最低价大，但是需要确保是满足最低价的最小价格！
    return dp[x - 1]


if __name__ == '__main__':
    n, x = map(int, input().strip().split(' '))
    arr = list(map(int, input().strip().split(' ')))
    ans = solution(n, x, arr)
    print(ans)
