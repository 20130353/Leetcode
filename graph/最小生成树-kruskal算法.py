# -*- coding: utf-8 -*-
# Author: sunmengxin
# time: 10/18/18
# file: 最小生成树-kruskal算法.py
# description:
# 确定新加入的顶点不会组成环！环按照并差集来做！

import numpy as np
import math
import copy as cp
import operator


class Edge():
    def __init__(self,s,e,w):
        self.s = s # start
        self.e = e # end
        self.w = w

def find_parent(parents,i):
    while parents[i] > 0:
        i = parents[i]
    return i

if __name__ == '__main__':
    n,m = input().split()
    n,m = int(n), int(m)

    edges = []
    for _ in range(m):
        x = input()
        # print(x.replace(' ','_'))
        a,b,w = x.split(' ')
        edge = Edge(int(a),int(b),int(w))
        edges.append(edge)

    edges_sorted = sorted(edges, key=operator.attrgetter('w'))
    parents = [-1 for _ in range(n)]
    for i in range(m):
        n = find_parent(parents,edges_sorted[i].s)
        m = find_parent(parents,edges_sorted[i].e)
        if n != m or m == -1 or n == -1:
            parents[n] = m
            print(n,end='\t')



'''
9 15
0 1 10
0 5 11
1 2 18
1 6 16
1 8 12
2 3 22
2 8 8
3 4 20
3 6 24
3 7 16
3 8 21
4 5 26
4 7 7
5 6 17
6 7 19
'''