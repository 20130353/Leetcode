# -*- coding: utf-8 -*-
# author: sunmengxin
# time: 18-11-25
# file: 反转单词
# description:

class Solution:
    def ReverseSentence(self, s):
        # write code here
        lmb = lambda x:x[::-1]
        return ' '.join(list(map(lmb,s[::-1].split(' '))))

if __name__ == '__main__':
    so = Solution()
    print(so.ReverseSentence('student. a am I'))