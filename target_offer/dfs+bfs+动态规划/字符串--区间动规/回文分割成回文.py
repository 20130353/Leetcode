#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 回文分割成回文.py
# @Author: smx
# @Date  : 2019/8/30
# @Desc  :

import copy as cp


class Palindrome_dfs:
    # 这里是为了得到可能的回文字符串！可以直接先用DP得到回文，之后直接使用！
    def get_huiwen(self, string):
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

    # DFS一直截取回文！
    def solution(self, string, ans, temp_ans):
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
        # 表示是否是回文
        dp = [[0] * n for _ in range(n)]
        # 回文的最少分割次数！
        dp_min = [n] * n
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if (a[i] == a[j]) and (i == j or i == j - 1 or dp[i + 1][j - 1] == 1):
                    dp[i][j] = 1
                if j == n - 1:
                    dp_min[i] = 0  # 本身是回文，所以不需要分割！
                else: # 在许多种分割方案中找到分割次数最少的方案
                    dp_min[i] = min(dp_min[i], dp_min[j + 1] + 1)
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
