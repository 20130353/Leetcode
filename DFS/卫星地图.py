# -*- coding: utf-8 -*-
# Author: sunmengxin
# time: 10/27/18
# file: 卫星地图.py
# description:

import re
import sys

#four direction
dir = [[0,1],[0,-1],[1,0],[-1,0]]
def DFS(n,m,x,y,now_num,ans,vis,mapa):

    # print 'x:%d \t y:%d \t ans:%d' %(x,y,ans[0])
    if now_num > ans[0]:
        ans[0] = now_num

    for i in range(4):
        nx = x + dir[i][0]
        ny = y + dir[i][1]
        if nx>=0 and ny>=0 and nx<m and ny<n and vis[nx][ny] == 0 and mapa[nx][ny] == '*':
            vis[nx][ny] = 1
            DFS(n,m,nx,ny,now_num+1,ans,vis,mapa)
            # vis[nx][ny] = 0
    return

if __name__ == '__main__':
    while True:
        try:
            ### input columns row
            n,m = list(map(int,input().strip().split()))
            mapa = []
            for i in range(m):
                strs = re.findall(r'.{1}', input().strip())
                mapa.append(strs)

            ###init
            vis = [[0 for i in range(n)] for j in range(m)]
            ans = [0]

            ###DFS
            for i in range(len(mapa)):
                for j in range(len(mapa[0])):
                    if mapa[i][j] == '*' and vis[i][j] == 0:
                        vis[i][j] = 1
                        DFS(n,m,i,j,1,ans,vis,mapa) # n,m,x,y,now_num,ans,vis,mapa
                        # vis[i][j] = 0

            sys.stdout.write('%d\n' %ans[0])
        except EOFError:
            raise

'''

10 5
..*.....**
.**..*****
..****.***
..****.***
.*...*....


'''