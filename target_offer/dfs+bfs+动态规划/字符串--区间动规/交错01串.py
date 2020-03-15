#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 交错01串.py
# @Author: smx
# @Date  : 2019/8/31
# @Desc  :
#


# 如果一个01串任意两个相邻位置的字符都是不一样的,我们就叫这个01串为交错01串。
# 例如: "1","10101","0101010"都是交错01串。
# 小易现在有一个01串s,小易想找出一个最长的连续子串,并且这个子串是一个交错01串。

class Mixture:
    def maxMixture(self, string, n):
        # dp[i]表示以a[i]作为最后一个字符的最长交错子串长度
        dp = [1] * n
        for i in range(1, n):
            if string[i] != string[i - 1]:
                dp[i] = dp[i - 1] + 1
        return max(dp)


if __name__ == '__main__':
    string = input().strip().replace(' ', '')
    ans = Mixture().maxMixture(string, len(string))
    print(ans)
