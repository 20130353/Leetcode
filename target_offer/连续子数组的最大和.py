# -*- coding: utf-8 -*-
# Author: sunmengxin
# time: 10/15/18
# file: 连续子数组的最大和.py
# description:

'''
    给定一个数组,输出数组中连续的子数组的最大和
'''

def max_subarray(data):
    # 以data[i]为最后一个元素的最大连续子区间和
    f = []
    for inx in range(len(data)):
        if inx == 0 or f[inx-1] < 0:
            f.append(data[inx])
        else:
            current = f[inx-1] + data[inx]
            f.append(current)
    return max(f)


if __name__ == '__main__':
    data = [1,-1,3,10,-4,7,2,-5]
    res = max_subarray(data)
    print(res)