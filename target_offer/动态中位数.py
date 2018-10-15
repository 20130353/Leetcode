# -*- coding: utf-8 -*-
# Author: sunmengxin
# time: 10/15/18
# file: 动态中位数.py
# description:

'''
    要求在O(logN)时间内插入删除元素,在O(1)时间内找到中位数
    解法:用两个小根堆对分别保存元素,堆顶就是中位数


    为了保证插入新数据和取中位数的时间效率都高效，这里使用大顶堆+小顶堆的容器，并且满足：
    1、两个堆中的数据数目差不能超过1，这样可以使中位数只会出现在两个堆的交接处；
    2、大顶堆的所有数据都小于小顶堆，这样就满足了排序要求。
    构建一个最大堆和一个最小堆，分别存储比中位数小的数和大的数。
    当目前两堆总数为偶数的时候，把数字存入最大堆，然后重排最大堆，如果最大堆的堆顶数字大于最小堆堆顶数字，
    则把两个堆顶数字交换，重排两堆，此时两堆数字总数为奇数，直接输出最大堆堆顶数字即为中位数；
    如果当前两堆总数为奇数的时候，把数字存入最小堆，重排最小堆，如果最大堆的堆顶数字大于最小堆堆顶数字，
    则把两个堆顶数字交换，重排两堆，此时两堆数字总数为偶数，取两堆堆顶数字做平均即为中位数
    最大堆堆顶元素要小于最小堆堆顶的元素，最大堆，堆顶元素最大，从大到小，最小堆堆顶元素最小，从小到大，这样的话，
    最大堆所有元素均小于最小堆了，中位数一定出现在两堆交替之间。

'''

def get_median(left,right,size):
    if size == 0:
        return
    if left == None or len(data) == 0:
        return right[0]
    if right == None or len(right) == 0:
        return left[0]
    max_heap(left)
    min_heap(right)
    # 如果小根堆的最大值 > 大根堆的最小值,说明两个堆不是顺序的 所有要交换直到两个堆都是顺序的
    while(True):
        if left[0] > right[0]:
            left[0],right[0] = right[0],left[0]
            max_heap(left)
            min_heap(right)
        else:
            break

    if size & 1 == 0:
        return (left[0] + right[0])/2
    else:
        return left[0]

def min_heap(data):

    # 建立小根堆
    # 从最后一个父节点开始不断调整堆的数值
    size = len(data)
    for i in range((size-1) // 2, -1, -1):
        # 开始调整堆
        while(True):
            min = i
            left = 2 * i + 1
            right = 2 * i + 2
            if left < size and data[min] > data[left]:
                min = left
            if right < size and data[min] > data[right]:
                min = right
            if min != i:
                data[min],data[i] = data[i],data[min]
                i = min
            else:
                break
    return

def max_heap(data):
    # 建立小根堆
    # 从最后一个父节点开始不断调整堆的数值
    size = len(data)
    for i in range(size // 2, -1, -1):
        # 开始调整堆
        while (True):
            max = i
            left = 2 * i + 1
            right = 2 * i + 2
            if left < size and data[max] < data[left]:
                max = left
            if right < size and data[max] < data[right]:
                max = right
            if max != i:
                data[max], data[i] = data[i], data[max]
                i = max
            else:
                break
    return



def solution(data):
    left = []
    right = []
    for i in range(len(data)):
        if i & 1 == 0:
            left.append(data[i])
        else:
            right.append(data[i])

    median = get_median(left,right,len(data))
    return median

if __name__ == '__main__':

    data = [3,4,2,5,7,9,1]
    data = []
    data = [1]
    res = solution(data)
    print(res)
    # 1,2,3,4,5,7,9