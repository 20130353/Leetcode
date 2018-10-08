# -*- coding: utf-8 -*-
# Author: sunmengxin
# time: 10/8/18
# file: BST.py
# description:

import numpy as np

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
            return False,node,parent
        if T.data == data:
            return True,node,parent
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

    def build_Tree(self, data):
        self.T = Node(data[0])
        for i in range(1,len(data)):
             self.T = self.insert_node(self.T,data[i])

    # def delete(self,root,data):
    #     flag,P,F = self.search_node(T,data)
    #     if P.lchild == None and P.rchild != None:
    #         T.rchild =
    #
    #     return

    def delete_node(self,data):
        if self.T.data == data:
            self.delete(self.T,data)
        elif self.T.data < data:
            self.delete_node(self.T.rchild)
        else:
            self.delete_node(self.t.lchild)



    def preorder_traverse(self,T):
        if T != None:
            print(T.data)
            self.preorder_traverse(T.lchild)
            self.preorder_traverse(T.rchild)

    def inorder_traverse(self,T):
        if T != None:
            self.inorder_traverse(T.lchild)
            print(T.data)
            self.inorder_traverse(T.rchild)

    def postorder_traverse(self,T):
        if T != None:
            self.postorder_traverse(T.lchild)
            self.postorder_traverse(T.rchild)
            print(T.data)

if __name__ == '__main__':
    # data = [62,88,58,47,35,73,51,99,37,93]
    data = [62,58,88,47,73,99,35,51,93,29,37,49,56,36,48,50]
    Tree = BST()
    Tree.build_Tree(data)
    Tree.inorder_traverse(Tree.T)
