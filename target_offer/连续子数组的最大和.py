# -*- coding: utf-8 -*-
# Author: sunmengxin
# time: 10/15/18
# file: 连续子数组的最大和.py
# description:

'''
    给定一个数组,输出数组中连续的子数组的最大和
'''

class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        res = []
        for inx,each in enumerate(array):
            if not res:
                res.append(each)
            else:
                res.append(max(each,each+res[-1]))
        # index = res.index(max(res))
        return max(res)



if __name__ == '__main__':
    data = [1,-1,3,10,-4,7,2,-5]
    so =Solution()
    res = so.FindGreatestSumOfSubArray(data)
    print(res)