# -*- coding: utf-8 -*-
# Author: sunmengxin
# time: 10/20/18
# file: 丑数.py
# description:
'''
    只包含因子2,3,5的数字叫做丑数求从小到达顺序的第1500个丑数
    解法1. 无限找每个数字.数字每次上加1,直到找个第1500个丑数
    解法2. 考虑丑数的全排列,用map或者set排除多余的丑数,然后排序得到第1500个
    解法3. 只考虑下一个丑数,直到1500个
    这里实现第三种解法
'''


# 反思：
# 1. 代码的每个相似变量的检查
class Solution:
    def GetUglyNumber_Solution(self, index):

        # write code here
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
