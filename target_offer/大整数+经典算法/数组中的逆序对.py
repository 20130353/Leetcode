# -*- coding: utf-8 -*-
# Author: sunmengxin
# time: 10/20/18
# file: 数组中的逆序对.py
# description:
'''
    两个数字如果前面的数字大于大于后面的数字就称为逆序对,求给定数组中的逆序对个数
    两种解法:
    1. 两个for 循环遍历
    2. 利用归并思想
'''

# 反思：list的数据分片只能是[:num]的形式，不能使用[a,b]
# 反思：递归忘记写结束条件了。

# 反思：这个方法会超时，但是时间复杂度已经是nlogn，还要怎么优化？
# 问题是数组的增删改查消耗时间,消除了数组的增删改查之后提升了25%的效率，但是还是超时！
# 减少时间消耗是要减少函数，我之前想减少数组的返回，但是不知道怎么减少，现在可以用传递参数的方式

# 反思：list的index存在错误是因为边界条件的问题

import time


# -*- coding:utf-8 -*-
class Solution:
    def merge_count(self, left, right):
        new = []
        count = 0

        i, j = 0, 0
        i_max, j_max = len(left), len(right)

        while i < i_max and j < j_max:
            if left[i] <= right[j]:
                new.append(left[i])
                i += 1
            else:
                new.append(right[j])
                j += 1
                count += i_max - i
        while (i < i_max):
            new.append(left[i])
            i += 1

        while (j < j_max):
            new.append(right[j])
            j += 1

        return count, new

    def inverse_pair(self, data):

        left, right = 0, len(data)
        if right == 1:
            return 0, data

        mid = int((left + right) / 2)
        cn1, left = self.inverse_pair(data[:mid])
        cn2, right = self.inverse_pair(data[mid:])
        count, sorted_arr = self.merge_count(left, right)
        return cn1 + cn2 + count, sorted_arr

    def InversePairs(self, data):
        if not data or len(data) <= 1:
            return 0
        else:
            count, sorted_data = self.inverse_pair(data)
            return (count) % (1000000007)

if __name__ == '__main__':
    so = Solution()
    # data = [364, 637, 341, 406, 747, 995, 234, 971, 571, 219, 993, \
    #         407, 416, 366, 315, 301, 601, 650, 418, 355, 460, 505, 360, \
    #         965, 516, 648, 727, 667, 465, 849, 455, 181, 486, 149, 588, 233, \
    #         144, 174, 557, 67, 746, 550, 474, 162, 268, 142, 463, 221, 882, 576, \
    #         604, 739, 288, 569, 256, 936, 275, 401, 497, 82, 935, 983, 583, 523, 697, \
    #         478, 147, 795, 380, 973, 958, 115, 773, 870, 259, 655, 446, 863, 735, 784,
    #         3, 671, 433, 630, 425, 930, 64, 266, 235, 187, 284, 665, 874, 80, 45, 848, 38, 811, 267, 575]


    data = [7, 8, 9, 1, 2, 3, 4]

    # start = time.time()
    print(so.InversePairs(data))
    # time_end = time.time() - start
    # print(time_end)
