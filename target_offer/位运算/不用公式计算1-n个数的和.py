# -*- coding: utf-8 -*-
# author: sunmengxin
# time: 18-11-25
# file: 不用公式计算1-n个数的和
# description:

# 反思:
# 1. 题目要求不能用加减乘除,那就用位运算和运算符
# 2. 题目要求不能用循环就用递归

class Solution:

    def __init__(self):
        self.tsum = 0

    def get_sum(self,n):
        self.tsum += n
        return n and self.Sum_Solution(n - 1)

    def Sum_Solution(self, n):
        # write code here
        self.get_sum(n)
        return self.tsum


if __name__ == '__main__':
    so = Solution()
    print(so.Sum_Solution(3))