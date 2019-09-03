#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 括号的匹配--数字.py
# @Author: smx
# @Date  : 2019/8/28
# @Desc  :

# 有两种想法：
# 1. dp[i]表示从0到字符i之间的匹配的最大长度，但是出现的问题是找下一个匹配的时候，会需要从上一次匹配的之前和之后找下一次可以匹配的点
# 2. dp[i]表示字符i作为这一次匹配的最后一个字符的匹配个数,出现的问题是如果这次匹配是在上次匹配之后,那么之前匹配的结果会丢失,所以需要加上之前的匹配

class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        # dp[i]表示以i为子字符串末尾时的最大长度
        if not s:
            return 0
        length = len(s)
        dp = [0 for __ in range(length)]

        for i in range(1, length):
            if s[i] == ")":
                j = i - 1 - dp[i - 1]  # 直接去查找前面的第n位，位移过了dp[i-1]位已经匹配的，直接过滤掉中间的(?
                print('{} {}'.format(i, j))
                if j >= 0 and s[j] == "(":  # 如果那位是‘（’则可以总数多+2
                    dp[i] = dp[i - 1] + 2
                    if j - 1 >= 0:
                        dp[i] += dp[j - 1]  # 重点，会把这次匹配之前的加进去，例如（）（（））, 如果这里不加，会缺少j之前的匹配数据
        print(dp)
        return max(dp)


if __name__ == '__main__':
    string = '()()()'
    string = '((()))()'
    # string = '(()())))()'
    #
    ans = Solution().longestValidParentheses(string)
    print(ans)
