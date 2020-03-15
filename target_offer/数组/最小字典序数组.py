#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 最小字典序数组.py
# @Author: smx
# @Date  : 2020/2/11
# @Desc  :
#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 雷火笔试题
# 数组n中的任意两个如果之和如果是奇数可以交换，不限制交换次数， 找到交换后的形成的字典序最小的数组
# 解体：模拟数组的各种场景
# 1. 如果数组只有奇数或者是偶数，那么就不能交换，返回原数组
# 2. 如果数组有奇数和偶数，可以变成任意字典序，直接返回排序后的数组就是最小值

def judge(arr):
    flag1, flag2 = False, False

    for each in arr:
        if each & 1 == 1:
            flag1 = True
        else:
            flag2 = True
    return flag1 and flag2


def find_arr(arr):
    flag = judge(arr)

    if flag:
        return sorted(arr)
    else:
        return arr


if __name__ == '__main__':
    arr = [8, 9, 1, 0, 4, 5, 3, 7]
    ans = find_arr(arr)
    print(ans)
