# -*- coding: utf-8 -*-
# Author: sunmengxin
# time: 10/26/18
# file: island_size.py
# description:

'''
给定一个包含了一些 0 和 1的非空二维数组 grid , 一个 岛屿 是由四个方向 (水平或垂直) 的 1 (代表土地) 构成的组合。你可以假设二维矩阵的四个边缘都被水包围着。

找到给定的二维数组中最大的岛屿面积。(如果没有岛屿，则返回面积为0。)

示例 1:

[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
对于上面这个给定矩阵应返回 6。注意答案不应该是11，因为岛屿只能包含水平或垂直的四个方向的‘1’。

示例 2:

[[0,0,0,0,0,0,0,0]]
对于上面这个给定的矩阵, 返回 0。

'''

'''
    出现的问题是: 
    1. 重复数'1',解决方案是删除回溯记号,标记过vis的区域不再计数
    2. 如果用不是返回DFS次数的话,会出现少数的情况,因为从下一层回来的之后,在进入当前层的下一层,sum传递的是当前层的数值,会少了之前的下一层结果!
    所以这个的解决方案就是 -a DFS传递返回值 -b DFS的sum是可修改的
    
    还有一个调试bug的好方法是: 打印i,j值,同时在ipad上对照原始的数组形式
'''
dir = [[0,1],[0,-1],[1,0],[-1,0]]
def DFS(i,j,map,vis, sum, max):

    print('i,j,sum:',i,j,sum[0])
    if sum[0] > max[0]:
        max[0] = sum[0]

    for inx in range(4):
        next_i = i + dir[inx][0]
        next_j = j + dir[inx][1]
        if next_i >= 0 and next_i < len(map) and next_j >= 0 and next_j < len(map[0])\
            and map[next_i][next_j] == '1' and vis[next_i][next_j] == False:
            vis[next_i][next_j] = True
            sum[0] = sum[0] + 1
            DFS(next_i, next_j, map, vis, sum, max)

if __name__ == '__main__':
    n = int(input().strip())
    map = []
    vis = []
    for _ in range(n):
        a = list(input().strip().replace(',',''))
        map.append(a)
        vis.append([False for _ in a])

    max = [0]
    for i in range(n):
        for j in range(len(map[i])):
            if map[i][j] == '1' and vis[i][j] == False:
                print('------------- start ------------')
                print(i,j)
                vis[i][j] = True
                sum = [1]
                DFS(i, j, map, vis, sum, max)
    print('max:',max[0])

'''

8 
0,0,1,0,0,0,0,1,0,0,0,0,0
0,0,0,0,0,0,0,1,1,1,0,0,0
0,1,1,0,1,0,0,0,0,0,0,0,0
0,1,0,0,1,1,0,0,1,0,1,0,0
0,1,0,0,1,1,0,0,1,1,1,0,0
0,0,0,0,0,0,0,0,0,0,1,0,0
0,0,0,0,0,0,0,1,1,1,0,0,0
0,0,0,0,0,0,0,1,1,0,0,0,0

'''
