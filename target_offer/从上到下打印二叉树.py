# -*- coding: utf-8 -*-
# Author: sunmengxin
# time: 10/14/18
# file: 从上到下打印二叉树.py
# description:

'''
    二叉树的层次遍历
'''
class Node:
    def __init__(self,data):
        self.data = data
        self.lchild = None
        self.rchild = None

class BST:
    def __init__(self):
        self.T = None

    def search_node(self,T,parent,data):
        if T == None:
            return False,T,parent
        if T.data == data:
            return True,T,parent
        if T.data < data:
            return self.search_node(T.rchild,T,data)
        else:
            return self.search_node(T.lchild,T,data)

    def insert_node(self,T,data):
        if T == None:
            return Node(data)
        else:
            if T.data < data:
                T.rchild = self.insert_node(T.rchild,data)
            else:
                T.lchild = self.insert_node(T.lchild,data)
        return T

    def build_tree(self, data):
        self.T = Node(data[0])
        for i in range(1,len(data)):
             self.T = self.insert_node(self.T,data[i])



    def print_level_tree(self,T):
        if T == None:
            return

        queue = [T]
        while len(queue) != 0:
            node = queue.pop(0)
            print(node.data)
            if node.lchild:
                queue.append(node.lchild)
            if node.rchild:
                queue.append(node.rchild)
        return

if __name__ == '__main__':
    # data = [1]
    data = [1,2,3,4,5,6,7]
    #

    Tree = BST()
    Tree.build_tree(data)
    Tree.print_level_tree(Tree.T)

