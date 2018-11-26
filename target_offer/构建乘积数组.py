# -*- coding: utf-8 -*-
# author: sunmengxin
# time: 18-11-26
# file: 构建乘积数组
# description:


# 反思:
# 1. 自己的想法只能实现o(n^2),想到优化的方式应该是本次在上一次的基础上优化,但是没想到是化成矩阵,然后计算上下三角的乘积

class Solution:
    def multiply(self, A):
        # write code here
        if not A:
            return []

        # 计算下三角
        # 从左到右
        num = len(A)
        B = [1 for _ in range(num)]
        for i in range(1, num):
            B[i] = B[i-1] * A[i-1]

        # 计算上三角
        # 自下而上
        # 保留上次的计算结果乘本轮新的数,因为只是后半部分进行累乘，所以设置一个tmp,能够保留上次结果
        tmp = 1
        for i in range(num-2, -1, -1):
            tmp *= A[i+1]
            B[i] *= tmp
        return B

if __name__ == '__main__':
    so = Solution()
    print(so.multiply([1,2,3]))