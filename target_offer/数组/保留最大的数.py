#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 保留最大的数.py
# @Author: smx
# @Date  : 2019/8/27
# @Desc  :

# 存在的问题：语法错误或者数组越界非法访问等情况 --》 输入有错，输入是两行！题目要求和给的测试案例不一定对应！
# 存在的问题：超时！ --》 不用两层for循环用not in判断
# 存在的问题：答案不正确！ --》
# 我自己的想法有错误，不能是排序得到答案，需要的将大的数字的位置提到前面来
# 自己的想法有错误，不是去掉比后面一个元素大的元素，是保留的元素要比其他的元素大
# 8215492
# 5
# 92 -- 是正确的，但是我自己不知道！

def solution(str_n, str_k):
    k = int(str_k)
    count = Counter(str_n)
    count = sorted(dict(count).items(), key=lambda x: x[0])

    # print(count)
    remove_list = []
    for each in count:
        # print(each)
        if k >= each[1]:
            remove_list.append(each[0])
            k -= each[1]
        else:
            break

    # print(remove_list)
    new_string = ''
    for each in str_n:
        if each not in remove_list:
            new_string += each
    return new_string


def solution1(str_n, str_k):
    if int(str_k) - 1 == len(str_n):
        return max(str_n)
    remove_list = sorted(str_n)[:int(str_k)]
    leave_list = []
    for i in range(len(str_n)):
        if str_n[i] not in remove_list:
            leave_list.append(str_n[i])
    return ''.join(leave_list)


def solution2(str_n, k):
    new_string = []
    n = len(str_n)
    for i in range(n):
        while k > 0 and new_string and new_string[-1] < str_n[i]:
            new_string.pop()
            k -= 1
        new_string.append(str_n[i])
    return ''.join(new_string[:len(new_string) - k])


if __name__ == '__main__':
    str_n = input()
    k = int(input())
    # str_n, str_k = input().strip().split(' ')
    new_string = solution2(str_n, k)
    print(new_string)

#
# 3251
# 1
# 351
#
# 3251
# 1
# 325
