# -*- coding: utf-8 -*-
# Author: sunmengxin
# time: 10/15/18
# file: 数组中出现次数超过一半的数.py
# description:

'''
    给定一个数组,求数组中出现次数超过一半的数
    解法1. 用哈希表存储每个数字出现的次数,找到出现次数最多的数字
    解法2. 出现次数最多的数字=中位数
    解法3. 出现次数大于其他数字的出现次数的总和
'''
# 哈希表
def solution1(data):
    dict = {}
    for each in set(data):
        dict[str(each)] = 0
    for i in range(len(data)):
        dict[str(data[i])] += 1

    sorted(dict.items(),key=lambda item:item[1])
    return int(list(dict.keys())[0])

# 出现次数大于其他数字的总和
def solution2(data):
    count = None
    for each in data:
        if count == None:
            count = {str(each):1}
        else:
            if list(count.keys())[0] == str(each):
                count[str(each)] += 1
            else:
                current = list(count.keys())[0]
                count[current] -= 1
                if count[current] == 0:
                    count = {str(each): 1}
    return int(list(count.keys())[0])

if __name__ == '__main__':
    data = [1,1,1,1,3,3]
    res = solution2(data)
    print(res)
