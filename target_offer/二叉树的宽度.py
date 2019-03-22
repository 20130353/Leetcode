# -*- coding: utf-8 -*-
# Author: sunmengxin
# time: 10/19/18
# file: 二叉树的宽度.py
# description:

'''
    求二叉树的宽度有两种解法:
    解法1. 递归用width+deepth的方式
    解法2. 非递归用队列的方式
'''


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def solution1(T, deepth, width):
    if T == None:
        width[deepth] = 0
        return

    if deepth == 0:
        width[0] = 1

    deepth += 1
    if T.left != None:
        width[deepth] += 1
        solution1(T.left, deepth, width)

    if T.right != None:
        width[deepth] += 1
        solution1(T.right, deepth, width)
    return


def solution2(T):
    if T == None:
        return 0

    queue = [T]
    max_width = 0
    while len(queue):
        size = len(queue)
        max_width = max(max_width, size)
        while size:
            top = queue[0]
            del queue[0]
            if top.left:
                queue.append(top.left)
            if top.right:
                queue.append(top.right)
            size -= 1
    return max_width


# 使用判断条件，条件一定要些的非常明确，不能使用简写。
class Solution:
    def get_width(self, T):
        if not T:
            return 0
        import queue
        mqueue = queue.Queue()
        mqueue.put(T)

        max_width = 0
        while mqueue.empty() == False:
            size = mqueue.qsize()
            max_width = max(max_width, size)
            while size > 0:
                top = mqueue.get()
                if top.left:
                    mqueue.put(top.left)
                if top.right:
                    mqueue.put(top.right)
                size -= 1
        return max_width


if __name__ == '__main__':
    root = Node(1)
    Node1 = Node(1)
    Node2 = Node(2)
    Node3 = Node(3)
    Node4 = Node(4)
    Node5 = Node(5)
    Node6 = Node(6)
    Node7 = Node(7)
    root.left = Node2
    root.right = Node3
    Node2.left = Node4
    Node2.right = Node5
    Node3.left = Node6
    Node3.right = Node7

    # width = [0 for _ in range(100)]
    # solution1(Node2,0,width)
    # max_width = max(width)
    # print(max_width)

    max_width = solution2(Node2)
    print(max_width)

    print(Solution().get_width(Node2))
