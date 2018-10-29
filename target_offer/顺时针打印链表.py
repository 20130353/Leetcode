# -*- coding: utf-8 -*-
# Author: sunmengxin
# time: 10/28/18
# file: 顺时针打印链表.py
# description:
'''
    输入一个矩阵，按照从外向里以顺时针的顺序依次扫印出每一个数字
    解题的时候要注意打印分为两步:
    1. 打印当前圈, 打印当前圈的时候小心圈可能会退化到不是完整的正方形,每输出一行或者一列的时候需要判断一下
    2. 打印坐标下移,打印下一圈

'''


def print_fun(data):
    if data == None or len(data) == 0:
        return

    x, y = 0, 0
    rows = (len(data) - 1)
    cols = (len(data[0]) - 1)

    while 2 * x <= rows and 2 * y <= cols:
        print_data(data, x, y)
        x += 1
        y += 1


def print_data(data, x, y):
    rows = len(data)
    cols = len(data[0])

    for j in range(y, cols - y):
        print(data[x][j], end='\t')

    # 环的高度至少为2,才能输出右边的一列
    if rows - x - 1 > x:
        for i in range(x + 1, rows - x):
            print(data[i][cols - y - 1], end='\t')

    # 环的高度和宽度至少是2,才能输出下边的一行
    if rows - x - 1 > x and cols - 1 - y > y:
        for j in range(cols - y - 2, y - 1, -1):
            print(data[rows - 1 - x][j], end='\t')

    # 环的宽度至少是2,环的宽度至少是3才能输出左边的一列
    if cols - 1 - y > y and rows - 1 - x > x + 1:
        for i in range(rows - 1 - x - 1, x, -1):
            print(data[i][y], end='\t')


if __name__ == '__main__':
    data = [[1, 2, 3, 4, 5, 6, 7, 8], [22, 23, 24, 25, 26, 27, 28, 9], \
            [21, 36, 37, 38, 39, 40, 29, 10], [20, 35, 34, 33, 32, 31, 30, 11], \
            [19, 18, 17, 16, 15, 14, 13, 12]]

    # data = [1, 2, 3, 4, 5, 6, 7, 8]
    #
    # data = [[1, 2, 3, 4, 5, 6, 7, 8], [16, 15, 14, 13, 12, 11, 10, 9]]
    #
    # data = [[1], [2], [3], [4], [5], [6], [7], [8]]
    #
    # data = [[0, 1], [15, 2], [14, 3], [13, 4], [12, 5], [11, 6], [10, 7], [9, 8]]

    # data = [[1, 2], [4, 3]]

    # data = [1]

    print_fun(data)
