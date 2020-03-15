# -*- coding: utf-8 -*-
# Author: sunmengxin
# time: 10/20/18
# file: 丑数.py
# description:
'''
    只包含因子2,3,5的数字叫做丑数求从小到达顺序的第1500个丑数
    解法1. 数字每次上加1,直到找个第1500个丑数
    解法3. 只考虑下一个丑数,直到1500个.
'''

# 核心思想是每个数都乘以2,3,5，下一个丑数一定在其中。用三个指针分别表示2,3,5乘到的位置。
class Solution:
    def GetUglyNumber_Solution(self, index):
        if index <= 0:
            return 0

        res = [1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15]
        if index < 11:
            return res[index - 1]

        index2, index3, index5 = 0, 0, 0
        next_index = 1
        res = [1 for _ in range(index)]
        while next_index < index:
            next_value = min(res[index2] * 2, res[index3] * 3, res[index5] * 5)
            res[next_index] = next_value
            while res[index2] * 2 <= next_value:
                index2 += 1
            while res[index3] * 3 <= next_value:
                index3 += 1
            while res[index5] * 5 <= next_value:
                index5 += 1
            next_index += 1
        return res[-1]


if __name__ == '__main__':
    so = Solution()
    print('第1500个丑数是:', so.GetUglyNumber_Solution(11))
