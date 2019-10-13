#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 回文添加一个字符让字符串变成回文串.py
# @Author: smx
# @Date  : 2019/8/30
# @Desc  : 牛客网题目名字：回文

# 您的代码已保存
# 答案错误:您提交的程序没有通过所有的测试用例
# case通过率为70.00%
# 用例:
# skwandroioukwyaimnsfuifqmivnkeewqwggcuinswauuaqw
# 对应输出应该为:
# 95
# 你的输出为:
# 78
# class Palindrome:
#     # 算法思路是先找到最长回文字串，然后找左右两边的字符交集，总长-交集*2=需要增加的字符
#     # 存在的问题：最长的回文子串可能存在多个，多个位置不一样，左右两边的交集就不一样，最靠近中心的回文是正确解。
#     # 存在的问题：靠近中心的回文不一定是正确解！是两边交集最大的才是正确解
#     def addLeastPalindrome(self, a, n):
#         dp = [[0] * n for _ in range(n)]
#         max_start, max_leng = [], 0
#         for i in range(n - 2, -1, -1):
#             for j in range(i, n):
#                 if (a[i] == a[j]) and (i == j or i == j - 1 or dp[i + 1][j - 1] == 1):
#                     dp[i][j] = 1
#                     if j - i + 1 > max_leng:
#                         max_leng = j - i + 1
#                         max_start = [i]
#                     elif j - i + 1 == max_leng:
#                         max_start.append(i)
#
#         min_leng = float('inf')
#         # 左右交集应该是以回文的中心算或者是减去回文的部分！
#         for pos in max_start:
#             lleft = string[:pos]
#             lright = string[pos + max_leng:]
#             print('lleft {},lright {},huiwen {}'.format(lleft, lright, string[pos:pos + max_leng]))
#             print('lleft leng {},lright leng {},huiwen leng{}'.format(len(lleft), len(lright),
#                                                                       len(string[pos:pos + max_leng])))
#             if len(lleft) <= len(lright):
#                 inter = [each for each in lleft if each in lright]
#             else:
#                 inter = [each for each in lright if each in lleft]
#             min_leng = min(n - len(inter) * 2 - max_leng + n, min_leng)
#         return min_leng


# 我的dp存在的问题初始值设置不对，也找不到路径
# 您的代码已保存
# 运行超时:您的程序未能在规定时间内运行结束，请检查是否循环有错或算法复杂度过大。
# case通过率为15.00%

# 改进加入n
# 答案错误:您提交的程序没有通过所有的测试用例
# case通过率为70.00%
# skwandroioukwyaimnsfuifqmivnkeewqwggcuinswauuaqw
# 77
# 错误的原因是：加完之后回文指针没有移动，所以出现指针错位的现象，所以得不到正确解！
# class Palindrome:
#     def addLeastPalindrome(self, a, n):
#         dp = [[0] * n for _ in range(n)]
#         for i in range(n - 2, -1, -1):
#             dp[i][i + 1] = 0 if a[i + 1] == a[i] else 1
#             for j in range(i + 1, n):
#                 if a[i] == a[j]:
#                     dp[i][j] = dp[i + 1][j - 1]
#                 else:
#                     dp[i][j] = min(dp[i][j - 1], dp[i + 1][j]) + 1
#         return dp[0][n - 1] + n


# 暴力解法 --> AC
# 暴力解法的核心：每个位置得到字符串+当前位置的反向组成新的回文串，判断最小的回文串长度
# 收获是回文串出现不相等的时候可以加左边或者加右边，就形成递归问题，为了避免递归问题，直接前后相加。
class Palindrome:
    def is_huiwen(self, string):
        i = 0
        leng = len(string)
        while i <= (leng // 2) and string[i] == string[leng - i - 1]:
            i += 1
        if i > (leng // 2):
            return True
        else:
            return False

    # 这里缺少了从右到左的过程，竟然也AC了。。
    def addLeastPalindrome(self, string, n):
        min_leng = float('inf')
        for i in range(string.__len__()):
            pre_string = string[:i]
            concat_string = string + pre_string[::-1]
            if self.is_huiwen(concat_string):
                min_leng = min(min_leng, concat_string.__len__())
        return min_leng


# 得到回文长度！
if __name__ == '__main__':
    try:
        while True:
            string = input().strip()
            ans = Palindrome().addLeastPalindrome(string, len(string))
            print(ans)
    except Exception as e:
        pass
