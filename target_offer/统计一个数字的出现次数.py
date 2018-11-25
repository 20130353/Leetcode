# -*- coding: utf-8 -*-
# author: sunmengxin
# time: 18-11-25
# file: 统计一个数字的出现次数
# description:

class Solution:
    def GetNumberOfK(self, data, k):
        # write code here


        import collections
        return collections.Counter(data)[k]



if __name__ == '__main__':


    so = Solution()
    print(so.GetNumberOfK([],4))