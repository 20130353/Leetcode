# -*- coding: utf-8 -*-
# Author: sunmengxin
# time: 10/19/18
# file: 机器人的运动范围.py
# description:

'''
    给定一个棋盘,要求机器人只能走上下左右的方向,不能进入到坐标之和等与s的方格,求机器人能进入多少方格?
'''

dir = [[0,1],[0,-1],[1,0],[-1,0]]
def DFS(map,i,j,s,count):
    n = len(map)
    for k in range(4):
        next_i = i + dir[k][0]
        next_j = j + dir[k][1]

        sum_ij = bit_sum(next_i) + bit_sum(next_j)
        if next_i>=0 and next_i < n and next_j >=0 and next_j < n and map[next_i][next_j] == 0 and sum_ij != s:
            map[next_i][next_j] = 1
            count[0] += 1
            DFS(map,next_i,next_j,s,count)

def bit_sum(a):
    if a < 10:
        return a
    else:
        s = 0
        while(a):
            s += a%10
            a /= 10
    return s

if __name__ == '__main__':

    n,s = input().split()
    n,s = int(n),int(s)

    map = [[0 for _ in range(n)] for _ in range(n)]

    map[0][0] = 1
    count = [1]
    DFS(map,0,0,s,count)
    print(count[0])