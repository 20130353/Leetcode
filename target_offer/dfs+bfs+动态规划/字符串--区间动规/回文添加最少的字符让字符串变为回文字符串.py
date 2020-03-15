# -*- coding: utf-8 -*-
# @File    : 回文添加最少的字符让字符串变为回文字符串.py
# @Author  : smx
# @Date    : 2019/10/13
# @Desc    :


# 两种解法总结：
# 1. 暴力遇到不合适的字符，尝试左加一个，右加一个，然后继续递归，找到最小的字符串
# 2. DP+回溯

# 错误的暴力解法
# 暴力解法的核心：每个位置得到字符串+当前位置的反向组成新的回文串，判断最小的回文串长度
# 收获是回文串出现不相等的时候可以加左边或者加右边，就形成递归问题，为了避免递归问题，直接前后相加。
# class Palindrome:
#     def is_huiwen(self, string):
#         i = 0
#         leng = len(string)
#         while i <= (leng // 2) and string[i] == string[leng - i - 1]:
#             i += 1
#         if i > (leng // 2):
#             return True
#         else:
#             return False
#
#     # 这种方式不会得到最优解，因为只翻转了一次！
#     def addLeastPalindrome(self, string):
#         min_leng = float('inf')
#         min_string = ''
#         for i in range(string.__len__()):
#             pre_string = string[:i]
#             concat_string = string + pre_string[::-1]
#             if len(concat_string) < min_leng and self.is_huiwen(concat_string):
#                 min_leng = concat_string.__len__()
#                 min_string = concat_string
#
#         for i in range(string.__len__(), -1, -1):
#             post_string = string[i:]
#             concat_string = post_string[::-1] + string
#             if len(concat_string) < min_leng and self.is_huiwen(concat_string):
#                 min_leng = concat_string.__len__()
#                 min_string = concat_string
#         return min_string

# 答案错误:您提交的程序没有通过所有的测试用例
# case通过率为0.00%
# def solution(string, i, j, min_leng, min_string):
#     # print('string {},i {},j {}'.format(string, i, j))
#     if len(string) >= min_leng[0]:
#         return
#     while i < len(string) and j >= 0 and i <= j and string[i] == string[j]:
#         i += 1
#         j -= 1
#     if i > j:
#         min_leng[0] = len(string)
#         min_string[0] = string
#     else:
#         solution(string[:j + 1] + string[i] + string[j + 1:], i + 1, j, min_leng, min_string)
#         solution(string[:i] + string[j] + string[i:], i, j + 1, min_leng, min_string)  # 因为在前面增加了一个字符，所以需要后移一位

# 运行超时:您的程序未能在规定时间内运行结束，请检查是否循环有错或算法复杂度过大。
# case通过率为0.00%
class Solution:
    def get_dp(self, a, n):
        dp = [[0] * n for _ in range(n)]  # 表示字符串i-j需要添加字符个数
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                if a[i] == a[j]:
                    dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i + 1][j]) + 1
        return dp[0][n - 1], dp

    def get_huiwen(self, string):
        num, dp = self.get_dp(string, len(string))
        res = [''] * (string.__len__() + num)
        left, right = 0, string.__len__() + num - 1
        i, j = 0, string.__len__() - 1
        while i <= j:
            if string[i] == string[j]:
                res[left] = string[i]
                res[right] = string[j]
                i += 1
                j -= 1
            elif dp[i + 1][j] < dp[i][j - 1]:
                res[left] = string[i]
                res[right] = string[i]
                i += 1
            else:
                res[left] = string[j]
                res[right] = string[j]
                j -= 1
            left += 1
            right -= 1
        return res


if __name__ == '__main__':
    string = input().strip()
    ans = Solution().get_huiwen(string)
    print(''.join(ans))
