# -*- coding: utf-8 -*-
# Author: sunmengxin
# time: 10/18/18
# file: 拓扑排序.py
# description: 一步一步地将入度为0的节点删除,直至没有入度为0的节点为止

class Edge:
    def __init__(self, vex, w, next):
        self.vex = vex
        self.w = w
        self.next = next


class Vex:
    def __init__(self, in_num, data, first_edge):
        self.in_num = in_num
        self.data = data
        self.first_edge = first_edge


if __name__ == '__main__':
    n, m = input().split()
    n, m = int(n), int(m)

    # for _ in range(m):
    #     x = input()
    #     a, b, w = x.split(' ')
    #     map[int(a)][int(b)] = int(w)
    #     map[int(b)][int(a)] = int(w)

    # 这里只是完成了拓扑排序的步骤,但是整个程序是不能运行的
    edge_list = []
    stack = []
    for i in range(n):
        if edge_list[i].in_num == 0:
            stack.append(i)

    while (len(stack) != 0):
        top = stack.pop()
        e = edge_list[top].first_edge
        while (e):
            k = e.vex
            edge_list[k].in_num -= 1
        for i in range(n):
            if edge_list[i].in_num == 0:
                stack.append(i)
