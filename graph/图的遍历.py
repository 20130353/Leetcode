# -*- coding: utf-8 -*-
# Author: sunmengxin
# time: 10/17/18
# file: 图的遍历.py
# description:
'''
    深度优先遍历和广度优先遍历
'''


# 递归遍历
def DFS(i,n,map,visit):

    for j in range(n):
        if map[i][j] == 1 and visit[j] == 0:
            visit[j] = 1
            print(j, end='\t')
            DFS(j,n,map,visit)
    return


# 有问题
# def DFS_stack(i,n,map,visit):
#     stack = [i]
#     while(len(stack) != 0):
#         i = stack[-1]
#         for j in range(n):
#             if visit[j] == 0 and map[i][j] == 1:
#                 stack.append(j)
#                 visit[j] = 1
#                 print(j,end='\t')
#         stack.pop()

def BFS(i,n,map,visit):
    queue = [i]
    while len(queue) != 0:
        i = queue[0]
        del queue[0]
        for j in range(n):
            if map[i][j] == 1 and visit[j] == 0:
                queue.append(j)
                visit[j] = 1
                print(j,end='\t')

if __name__ == '__main__':

    n,m = input().split()
    n,m = int(n), int(m)
    map = [[-1 for _ in range(n)] for _ in range(n)]
    visit = [0 for _ in range(n)]
    for _ in range(m):
        a,b = input().split(' ')
        map[int(a)-1][int(b)-1] = 1
        map[int(b)-1][int(a)-1] = 1

    # for i in range(n):
    #     if visit[i] == 0:
    #         visit[i] = 1
    #         print(i,end='\t')
    #         DFS+BFS(i,n,map,visit)

    for i in range(n):
        if visit[i] == 0:
            visit[i] = 1
            print(i,end='\t')
            BFS(i,n,map,visit)

'''
9 14
1 2
1 6
2 3
2 7
2 9
3 4
3 9
4 5
4 7
4 8
4 9
5 6
5 8
6 7
'''

