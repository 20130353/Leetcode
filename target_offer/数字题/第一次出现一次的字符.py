# -*- coding: utf-8 -*-
# author: sunmengxin
# time: 18-11-23
# file: 第一次出现一次的字符
# description:

# 反思：计算字符串的字符出现的个数的函数是count

class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        for inx,each in enumerate(s):
            if s.count(each) == 1:
                return inx
        return -1

if __name__ == '__main__':
    so = Solution()
    print(so.FirstNotRepeatingChar('fadafa'))