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

def matrix_search(data,key):

    if data == None or len(data) == 0 or type(key).__name__ not in ['float','int','int64','long','complex']:
        return False
    data = np.array(data)
    rows,cols = data.shape
    i = 0
    j = cols - 1

    while( j>=0 and i <rows):
        if type(data[i,j]).__name__ not in ['float','int','int64','long','complex']:
            print('the type of value should be \'float\' or \'int\'')
            return False

        if data[i,j] > key:
            j -= 1
        elif data[i,j] < key:
            i += 1
        else:
            return True
    return False




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

    print(matrix_search(array, 10))
    print(matrix_search(array, 30))
    print(matrix_search(array, 13.0))
    print(matrix_search(array, ''))
    print(matrix_search(array2, 10))
    print(matrix_search(array3, 'b'))
    print(matrix_search(array4, 81))

