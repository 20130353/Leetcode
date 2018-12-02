# -*- coding: utf-8 -*-
# Author: sunmengxin
# time: 10/20/18
# file: x 出现的数目.py
# description:
'''
    给定一个数字n,m,求从1到n出现的m的次数
    1. 对每个数字求一遍出现m的次数,最后累加
    2. 直接计算数字的规律
    这里实现第二种解法
'''


class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        import math
        target = 1

        if n <= 0 or target < 0 or target > 9:
            return 0

        bits = 0
        temp = n
        while temp:
            bits += 1
            temp //= 10

        total = 0
        for i in range(1, bits + 1):
            high = n // math.pow(10, i)
            low = (n % math.pow(10, i)) % math.pow(10, i - 1)
            cut = (n // math.pow(10, i - 1)) - (n // math.pow(10, i)) * 10
            if cut == target:
                total += high * math.pow(10, i - 1) + low + 1
            elif cut < target:
                total += high * math.pow(10, i - 1)
            else:
                total += (high + 1) * math.pow(10, i - 1)

        return total


if __name__ == '__main__':
    count = Solution().NumberOf1Between1AndN_Solution(2593, 5)
    print(count)

    # print(259+260+294)
