#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 交错01串.py
# @Author: smx
# @Date  : 2019/8/31
# @Desc  :

class Mixture:
    # 思考这个问题的方式是：从最简单的问题开始，加一个字符的方式，加两个字符的方式
    # 答案错误: 您提交的程序没有通过所有的测试用例
    # case通过率为40.00 %
    # 存在的问题：子串写成子序列了
    def maxMixture(self, string, n):
        dp = [1] * n
        for i in range(1, n):
            if string[i] != string[i - 1]:
                dp[i] = dp[i - 1] + 1
        return max(dp)


if __name__ == '__main__':
    string = input().strip().replace(' ', '')
    ans = Mixture().maxMixture(string, len(string))
    print(ans)
