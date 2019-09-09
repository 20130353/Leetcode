# -*- coding: utf-8 -*-
# author: sunmengxin
# time: 18-11-16
# file: 只出现一次的数字
# description:

# encoding=utf8
'''
题目：一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。
要求时间复杂度是O(n)，空间复杂度是O(1)。
'''


def find_two_unique_num(num_list):
    result = 0
    for num in num_list:
        result ^= num
    lowbit = find_lowest_bit(result)
    result_1 = 0
    result_2 = 0
    for num in num_list:
        if num & lowbit != 0:
            result_1 ^= num
        else:
            result_2 ^= num
    return (result_1, result_2)


def find_lowest_bit(num):
    index = 0
    while num & 1 == 0:
        num = num >> 1
        index = 1
    return 1 << index


if __name__ == '__main__':
    num_list_1 = [2, 2, 1, 3]
    num_list_2 = [2, 4, 3, 6, 3, 2, 5, 5]
    print (find_two_unique_num(num_list_1))
    print (find_two_unique_num(num_list_2))
