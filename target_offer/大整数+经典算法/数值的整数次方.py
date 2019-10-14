# -*- coding: utf-8 -*-
# Author: sunmengxin
# time: 10/15/18
# file: 数值的整数次方.py
# description:

'''
    实现power函数
    解法1.将指数分成正负,分别求他们的乘积
    解法2.用递归的方式划分
'''

# AC!
class Solution:
    def mulity(self, base, n):
        if n == 0:
            return 1
        if n == 1:
            return base
        if n & 1 == 1:
            part = self.mulity(base, n // 2)
            return part * part * base
        else:
            part = self.mulity(base, n // 2)
            return part * part

    def Power(self, base, n):
        if n == 0:
            return 1
        if n == 1:
            return base
        if n < 0:
            return 1 / self.mulity(base, -n)
        else:
            return self.mulity(base, n)


if __name__ == '__main__':
    # ans = solution(1, 1)
    # ans = solution(2, 3)
    # ans = solution(3, -2)
    ans = Solution().Power(3, 0)
    print(ans)
