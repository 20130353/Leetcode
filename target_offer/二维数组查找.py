# -*- coding: utf-8 -*-
# Author: sunmengxin
# time: 10/9/18
# file: 二维数组查找.py
# description:

'''
在一个二维数组中，每一行都按照从左到右递增的顺序排序
每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
'''

'''
查找方式从右上角开始查找
如果当前元素大于target, 左移一位继续查找
如果当前元素小于target, 下移一位继续查找
进行了简单的修改, 可以判定输入类型为字符的情况
'''

import numpy as np

class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        if len(array) == 0:
            return False

        max_i, min_j = len(array) - 1, 0
        i, j = 0, len(array[0]) - 1
        while (True):
            while i <= max_i and array[i][j] < target:
                i += 1
            if i > max_i:
                return False
            if array[i][j] == target:
                return True

            while j >= min_j and array[i][j] > target:
                j -= 1

            if j < min_j:
                return False
            if array[i][j] == target:
                return True


if __name__ == '__main__':
    array = [[1, 2, 8, 9],
             [2, 4, 9, 12],
             [4, 7, 10, 13],
             [6, 8, 11, 15]]
    array2 = []
    array3 = [['a', 'b', 'c'],
              ['b', 'c', 'd']]
    array4 = [[62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80],
              [63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81],
              [64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82],
              [65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83],
              [66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84],
              [67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85]]

    # print(matrix_search(array, 10))
    # print(matrix_search(array, 30))
    # print(matrix_search(array, 13.0))
    # print(matrix_search(array, ''))
    # print(matrix_search(array2, 10))
    # print(matrix_search(array3, 'b'))
    # print(matrix_search(array4, 81))

    # so = Solution()
    # print(so.Find(20, array4))

    print([1,2,3][::-1])