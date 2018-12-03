# -*- coding: utf-8 -*-
# author: sunmengxin
# time: 18-11-26
# file: template
# description:

'''
    BFS和DFS的代码最大区别是:
    BFS使用的队列
    DFS使用的栈

'''


def BFS(graph,start):
    queue = []
    queue.append(start)
    visit_nodes = set()
    visit_nodes.add(start)
    while queue:
        vertex = queue.pop(0)
        nodes = graph[vertex]
        for node in nodes:
            if node not in visit_nodes:
                queue.append(node)
                visit_nodes.add(node)
        print(vertex, end='\t')
    print()

def DFS(graph,start):
    stack = []
    stack.append(start)
    visit_nodes = set()
    visit_nodes.add(start)
    while stack:
        vertex = stack.pop()
        nodes = graph[vertex]
        for node in nodes:
            if node not in visit_nodes:
                stack.append(node)
                visit_nodes.add(node)
        print(vertex,end='\t')



if __name__ == '__main__':
    graph = {
        'A':['B','C'],
        'B':['A','C','D'],
        'C':['A','B','D','E'],
        'D':['B','C','E','F'],
        'E':['C','D'],
        'F':['D']
    }

    BFS(graph,'A')
    DFS(graph,'A')


