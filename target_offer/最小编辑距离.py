# -*- coding: utf-8 -*-
# Author: sunmengxin
# time: 10/28/18
# file: 最小编辑距离.py
# description:

'''
    求：把 a 转换成 b 的最小操作次数，也就是所谓的最小编辑距离。
    举例： "xy" => "xz"，只需要把 y 替换成 z，因此，最小编辑距离为 1。
    "xyz" => "xy"，只需要删除 z ，因此，最小编辑距离为 1。

'''


def edit_distance(A, B):
    # print('A,B:', A, B)

    if len(A) == 0 and len(B) == 0:
        return 0
    if len(B) == 0 and len(A):
        return len(A)
    if len(A) == 0 and len(B):
        return len(B)
    if A[-1] == B[-1]:
        return edit_distance(A[:-1], B[:-1])
    else:
        res1 = edit_distance(A[:-1], B)
        res2 = edit_distance(A, B[:-1])
        res3 = edit_distance(A[:-1], B[:-1])
        # print('1,2,3:', res1, res2, res3)
        return min(res1, res2, res3) + 1


if __name__ == '__main__':
    A, B = [''], ['a']
    # A, B = ['a', 'b', 'c'], ['a']
    # A, B = ['a', 'b', 'c', 'f'], ['a', 'g']

    res = edit_distance(A, B)
    print(res)
