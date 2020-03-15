#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 最小平方数和.py
# @Author: smx
# @Date  : 2019/8/15
# @Desc  :

# 腾讯面试题
# 给一个正整数 n, 找到若干个完全平方数(比如1, 4, 9, ... )使得他们的和等于 n。你需要让平方数的个数最少。
# 例如：给出 n = 12, 返回 3 因为 12 = 4 + 4 + 4。
#     给出 n = 13, 返回 2 因为 13 = 4 + 9。

#  存在的问题：因为即使是从最大的开始找，但是找到的不一定是组合数量最小的 -》 直接暴力模拟所有的情况！
# 总结：这道题其实不难，所以当时没有做出来（没有做对）是考虑的情况少了，下次应该直接暴力模拟，然后在想优化！

def solution(num):
    dp = [0] * num
    for i in range(num):
        j = 1
        while i - j ** 2 >= 0:
            if dp[i] == 0:
                dp[i] = dp[i - j ** 2] + 1
            else:
                dp[i] = min(dp[i], dp[i - j ** 2] + 1)
            j += 1
    return dp[num - 1]


if __name__ == '__main__':
    num = 1
    # num = 50
    # num = 12
    ans = solution(num)
    print(ans)
