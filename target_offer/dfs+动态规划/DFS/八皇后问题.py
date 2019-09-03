# -*- coding: utf-8 -*-
# Author: sunmengxin
# time: 10/14/18
# file: 八皇后问题.py
# description:

def check(arr, row, col):
    # 检查当前皇后的位置和之前皇后的位置是否存在对角线冲突
    for pre_row in range(row):
        if abs(arr[pre_row] - col) == abs(pre_row - row):
            return False
    return True


def eight_queen(arr, row, n, ans_count):
    if row == n:
        global count
        count += 1
        if ans_count == count:
            print(''.join([str(each + 1) for each in arr]))
            ans_count = -1
        return

    if ans_count == -1:
        return

    for col in range(n):
        if col not in arr and check(arr, row, col) is True:
            arr[row] = col
            eight_queen(arr, row + 1, n, ans_count)
            arr[row] = -1

if __name__ == '__main__':
    count, n = 0, 8
    map = [-1 for _ in range(n)]
    ans_count = int(input().strip())
    eight_queen(map, 0, n, ans_count)
