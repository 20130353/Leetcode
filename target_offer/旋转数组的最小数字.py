# -*- coding: utf-8 -*-
# Author: sunmengxin
# time: 10/10/18
# file: 旋转数组的最小数字.py
# description:


'''
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。
例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。
'''

import numpy as np

def minvalue(data):

    if len(data) == 0 or data == None:
        return 0

    start = 0
    end = len(data) - 1
    if data[start] < data[end]:
        return data[start]

    minv = data[start]
    while( end - start > 1):
        mid = np.int((start + end)/2)

        # 中间的元素比尾巴的元素大，说明小的元素在中间元素和尾巴元素之间，所以start移动
        if data[mid] > data[end]:
            start = mid
        # 中间的元素比开始的元素小，说明最小元素在开始元素和中间元素之间
        elif data[mid] < data[start]:
            end = mid
        elif data[start] == data[mid] and data[mid] == data[end]:
            for i in range(start,end):
                if data[i] < minv:
                    minv = data[i]
                    end = i

    minv = data[end]
    return minv


if __name__ == '__main__':

    print(minvalue([3, 4, 5, 1, 2]))
    print(minvalue([1, 2, 3, 4, 5]))
    print(minvalue([1, 1, 1, 0, 1]))
    print(minvalue([1, 0, 1, 1, 1]))
    print(minvalue([]))
    print(minvalue([1]))