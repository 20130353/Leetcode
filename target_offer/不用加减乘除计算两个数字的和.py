# -*- coding: utf-8 -*-
# author: sunmengxin
# time: 18-11-26
# file: 不用加减乘除计算两个数字的和
# description:


# 反思:
# 1. 算法运行时间过大是因为没有取余 %0x100000000
# 2. 运算时碰到负数的时候结果总是出错，原因是取余时候写成100000000了，注意是0x100000000

class Solution:
    def Add(self, num1, num2):
        if num1 == 0:
            return num2
        if num2 == 0:
            return num1

        while num2:
            carry = (num1 & num2) << 1  # 两个数字相与计算进位
            num1 = (num1 ^ num2)%0x100000000  # 两个数字异或计算和
            num2 = carry%0x100000000
        return num1 if num1<=0x7FFFFFFF else num1 |(~0x100000000+1)

if __name__ == '__main__':
    so = Solution()
    print(so.Add(300,2))