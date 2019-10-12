# -*- coding: utf-8 -*-
# author: sunmengxin
# time: 18-11-15
# file: 斐波那契数列
# description:


# # 刚开始代码出错是因为for循环的字母写错了！！！
# class Solution:
#     def Fibonacci(self, n):
#         # write code here
#         F = [0,1,1,2,3,5,8,13,21,34]
#         if n < 10:
#             return F[n]
#         else:
#             # 这段代码违法
#             for i in range(10,n+1):
#                 F.append(F[i-1] + F[i-2])
#
#             return F[n]

# 这个题目最好的写法是不要用递归，用循环
class Solution:
    def Fibonacci(self, n):
        # write code here
        F = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        if n < 10:
            return F[n]
        else:
            pre = 34
            prepre = 21
            for i in range(10, n + 1):
                F.append(pre + prepre)
                prepre = F[-2]
                pre = F[-1]
            return F[n]



# LRU 删除最远不会被访问到的元素,当内存满了的话,直接删除最远的元素
# 双链表





if __name__ == '__main__':
    so = Solution()
    print(so.Fibonacci(30))
