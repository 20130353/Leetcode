# -*- coding: utf-8 -*-
# Author: sunmengxin
# time: 10/10/18
# file: 变态青蛙跳.py
# description:

def jump(n):
    if n <= 0:
        return 0
    else:
        return 2**(n-1)

class Solution:
    def jumpFloor(self, number):
        # write code here
        F = [0, 1, 3]
        if number < 2:
            return F[number]
        for i in range(3,number+1):
            F.append(F[i-1]+F[i-2])
        return F[number]

if __name__ == '__main__':
    # print(jump(0))
    # print(jump(1))
    # print(jump(2))
    # print(jump(3))
    # print(jump(100))


    so = Solution()
    print(so.jumpFloor(5))