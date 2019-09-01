#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 公平划分--数字.py
# @Author: smx
# @Date  : 2019/8/17
# @Desc  :

# 存在的问题是：只考虑了选择k，但是没有考虑另一个集合的元素是否完整
# 存在的问题是：集合的边界错误，导致case过不了！下次应该自己多写几个案例。不要考虑异常的case，要多些几个正常的case
# 存在的问题：超时！用找到两个集合，计算每个元素的偏差，可以改成找到一个集合，直接在原来的数组上遍历计算就可以了
# 还是超时！  这个是用C语言就可以解决！ 但是python语言就是不行！
# 可能问题可以转化化成另一个问题！

def solution(arr, n, k, pos, N1, sel):
    if k == 0:
        dis = 0
        no_sel = [each for each in arr if each not in sel]
        for i in sel:
            for j in no_sel:
                dis += abs(i - j)
        global min_dis
        min_dis = min(min_dis, dis)
        # print('N1 {}, N2 {}, dis {}'.format(sub1, sub2, dis))

    if pos + 1 <= n:
        N1[pos] = True
        sel.append(arr[pos])
        solution(arr, n, k - 1, pos + 1, N1, sel)

        N1[pos] = False
        sel.pop()
        solution(arr, n, k, pos + 1, N1, sel)

if __name__ == '__main__':
    n, k = map(int, input().strip().split(' '))
    arr = list(map(int, input().strip().split(' ')))

    min_dis = float('inf')
    solution(arr, n, k, 0, [False] * n, [])
    print(min_dis)
