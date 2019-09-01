#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 回文添加最少的字符让字符串变成回文串.py
# @Author: smx
# @Date  : 2019/8/30
# @Desc  :

# 您的代码已保存
# 答案错误:您提交的程序没有通过所有的测试用例
# case通过率为70.00%
# 用例:
# skwandroioukwyaimnsfuifqmivnkeewqwggcuinswauuaqw
# 对应输出应该为:
# 95
# 你的输出为:
# 78

class Palindrome:
    # 算法思路是先找到最长回文字串，然后找左右两边的字符交集，总长-交集*2=需要增加的字符
    # 存在的问题：最长的回文子串可能存在多个，多个位置不一样，左右两边的交集就不一样，最靠近中心的回文是正确解。
    def addLeastPalindrome(self, a, n):
        dp = [[0] * n for _ in range(n)]
        max_start, max_leng = 0, 0
        center = n // 2
        for i in range(n - 2, -1, -1):
            for j in range(i, n):
                if (a[i] == a[j]) and (i == j or i == j - 1 or dp[i + 1][j - 1] == 1):
                    dp[i][j] = 1
                    if j - i + 1 > max_leng:
                        max_leng = j - i + 1
                        max_start = i
                    elif j - i + 1 == max_leng and abs(max_start - center) > abs(i - center):
                        max_start = i

        lleft = string[:max_start]
        lright = string[max_start + max_leng:]
        if len(lleft) <= len(lright):
            inter = [each for each in lleft if each in lright]
        else:
            inter = [each for each in lright if each in lleft]
        return n - len(inter) * 2 - max_leng + n


# 我的dp存在的问题初始值设置不对，也找不到路径
# 您的代码已保存
# 运行超时:您的程序未能在规定时间内运行结束，请检查是否循环有错或算法复杂度过大。
# case通过率为15.00%
class Palindrome:
    def addLeastPalindrome_back(self, a, n):
        dp = [[0] * n for _ in range(n)]
        for i in range(n - 2, -1, -1):
            dp[i][i + 1] = 0 if a[i + 1] == a[i] else 1
            for j in range(i + 1, n):
                if a[i] == a[j]:
                    dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = min(dp[i][j - 1], dp[i + 1][j]) + 1

        for each in dp:
            print(each)

        new_leng = n + dp[0][n - 1]
        i, j = 0, n - 1
        ans_i, ans_j = 0, new_leng - 1
        ans = ['0'] * new_leng
        while i <= j:
            if a[i] == a[j]:
                ans[ans_i] = a[i]
                ans[ans_j] = a[j]
                i += 1
                j -= 1
            elif dp[i][j - 1] < dp[i - 1][j]:
                ans[ans_i] = a[j]
                ans[ans_j] = a[j]
                j -= 1
            else:
                ans[ans_i] = a[i]
                ans[ans_j] = a[i]
                i += 1
            ans_i += 1
            ans_j -= 1
        return ''.join(ans)


if __name__ == '__main__':
    try:
        while True:
            string = input().strip()
            ans = Palindrome().addLeastPalindrome(string, len(string))
            print(ans)
    except Exception as e:
        pass
