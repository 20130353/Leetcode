# -*- coding: utf-8 -*-
# Author: sunmengxin
# time: 10/14/18
# file: 八皇后问题.py
# description:

'''
    八皇后问题,8*8的棋盘要放置8个棋子,每行每列每个对角线只能放置一个棋子,不能重复
'''

import numpy as np
def diagonal_conflict(map, pos, index):

    # 检查当前皇后的位置和之前皇后的位置是否存在对角线冲突
    # i-j == column[i] - column[j]
    for i in range(index):
        if np.abs(i-index) == np.abs(map[i]-pos):
            return True

    return False

def eight_queen(map,bools,index):

    if index == 8:
        for each in map:
            print(each,end='')
        print('\n')
        return

    for i in range(1,9):
        if bools[i] == False and diagonal_conflict(map,i,index) == False:
            bools[i] = True
            map[index] = i
            eight_queen(map,bools,index+1)
            bools[i] = False
    return

if __name__ == '__main__':

    map = [0 for _ in range(8)]
    bools = [False for _ in range(9)]
    eight_queen(map,bools,0)
