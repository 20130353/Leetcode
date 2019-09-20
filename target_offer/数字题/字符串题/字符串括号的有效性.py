# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
# # @File  : 字符串括号的有效性.py
# # @Author: smx
# # @Date  : 2019/8/31
# # @Desc  :
#
#
# # dp的作用是找到之前匹配的最后位置，所以dp[i]表示以i作为结尾，连续括号匹配的最大长度
# # 您的代码已保存
# # 答案错误:您提交的程序没有通过所有的测试用例
# # case通过率为0.00%
#   循环输入存在问题！
# import re
# # class Solution(object):
# #     def validParentheses(self, a, n):
# #         if re.search(r'[^()]', a) is False or n & 1 == 1:
# #             return 'NO'
# #
# #         dp = [0] * n
# #         for i in range(1, n):
# #             j = i - 1 - dp[i - 1]
# #             if a[i] == ')' and j >= 0 and a[j] == '(':
# #                 dp[i] = dp[i - 1] + 2
# #                 if j - 1 >= 0:
# #                     dp[i] += dp[j - 1]
# #         # for each in dp:
# #         #     print(each)
# #         return 'YES' if max(dp) == n else 'NO'
#
class Solution(object):
    # 存在的问题：实现不需要栈，就需要记录一下（的数量
    # def validParentheses(self, string, n):
    #     if n & 1 == 1:
    #         return False
    #     stack = []
    #     for i in range(n):
    #         if string[i] == '(':
    #             stack.append('(')
    #         elif string[i] == ')':
    #             if stack.__len__() >= 1 and stack[-1] == '(':
    #                 stack.pop()
    #             else:
    #                 return False
    #         else:
    #             return False
    #     return True if stack.__len__() == 0 else False

    def validParentheses(self, string, n):
        if n & 1 == 1:
            return False
        num = 0
        for i in range(n):
            if string[i] == '(':
                num += 1
            elif string[i] == ')':
                num -= 1
                if num < 0:
                    return False
            else:
                return False
        return True if num == 0 else False

if __name__ == '__main__':
    string = input().strip()
    ans = Solution().validParentheses(string, len(string))
    print('YES') if ans else print('NO')
