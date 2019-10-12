#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 回文分割成回文.py
# @Author: smx
# @Date  : 2019/8/30
# @Desc  :


# 您的代码已保存
# 运行超时:您的程序未能在规定时间内运行结束，请检查是否循环有错或算法复杂度过大。
# case通过率为0.00%
# 存在的问题：时间复杂度太大 --> 直接记录最长回文串的位置
#
# 运行超时:您的程序未能在规定时间内运行结束，请检查是否循环有错或算法复杂度过大。
# case通过率为0.00%
# 存在的问题：时间复杂度太大 --> 可以把遍历dp和找最大分割的次数两个操作合并-->不能合并，因为dp是从n-1，递减到0的
# 可以合并，用一个dp保存最少分割次数
# 还是复杂度过大

#将一个数组拆成都是回文的子数组
# 一种思想：将字符串拆成回文，然后递归剩下的部分
# 优化：判断是否是回文用DP
# 优化：递归剩下的部分用min DP
import copy as cp
class Palindrome_dfs:
    def get_huiwen(self,string):
        if len(string) <= 0:
            return 0
        ans = []
        for inx in range(len(string)):
            low, high = 0, inx
            while low < high and low < len(string) and high >= 0 and string[low] == string[high]:
                low += 1
                high -= 1
            if string[low] == string[high]:
                ans.append(inx)
        return ans

    def solution(self,string, ans, temp_ans):
        if not string:
            return
        if len(string) == 1:
            ans.append(temp_ans + list(string))
            return
        inxs = self.get_huiwen(string)
        for each in inxs:
            if each + 1 < len(string):
                each_ans = cp.deepcopy(temp_ans)
                each_ans.append(string[:each + 1])
                self.solution(string[each + 1:], ans, each_ans)

class Palindrome:
    def palindromeLearstNum(self, a, n):
        dp = [[0] * n for _ in range(n)]
        dp_min = [n] * n
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if (a[i] == a[j]) and (i == j or i == j - 1 or dp[i + 1][j - 1] == 1):
                    dp[i][j] = 1
                if j == n - 1:
                    dp_min[i] = 0
                else:
                    dp_min[i] = min(dp_min[j + 1] + 1, dp_min[i])
        return dp_min[n - 1]


if __name__ == '__main__':
    try:
        while True:
            # string = 'cbabdf'
            # string = 'aaaa'
            # string = 'abcabccbadda'
            # string = 'ABCBAEEE'
            string = input().strip()
            ans = Palindrome().palindromeLearstNum(string, len(string))
            print(ans)
    except Exception as e:
        pass
