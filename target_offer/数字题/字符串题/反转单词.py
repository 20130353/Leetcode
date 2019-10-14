# -*- coding: utf-8 -*-
# author: sunmengxin
# time: 18-11-25
# file: 反转单词
# description:

class Solution:
    def ReverseSentence(self, s):
        return ' '.join(list(s.split(' '))[::-1])


if __name__ == '__main__':
    so = Solution()
    print(so.ReverseSentence('student. a am I'))
