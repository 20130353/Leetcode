# -*- coding: utf-8 -*-
# Author: sunmengxin
# time: 10/8/18
# file: AVL.py
# description: the speed of search of numerous random samples is faster than BST(binary search tree)

import numpy as np

class Node:
    def __init__(self,data):
        self.data = data
        self.lchild = None
        self.rchild = None
        self.height = 1

class AVL:
    def __init__(self):
        self.T = None

    def single_left_rotate(self,T):
        R = T.rchild
        T.rchild = R.lchild
        R.lchild = T
        # T.height = max(self.cal_height(T.lchild),self.cal_height(T.rchild))+1
        R.height = max(self.cal_height(R.lchild),self.cal_height(R.rchild))+1
        return R

    def single_right_rotate(self,T):
        L = T.lchild
        T.lchild = L.rchild
        L.rchild = T
        # T.height = max(self.cal_height(T.lchild),self.cal_height(T.rchild))+1
        L.height = max(self.cal_height(L.lchild),self.cal_height(L.rchild))+1
        return L

    def double_left_rotate(self,T):
        T.rchild = self.single_right_rotate(T.rchild)
        return self.single_left_rotate(T)

    def double_right_rotate(self,T):
        T.lchild = self.single_left_rotate(T.lchild)
        return self.single_right_rotate(T)

    def insert_node(self, T, data):
        if T == None:
            return Node(data)
        else:
            return self._insert(T, data)

    def cal_height(self,T):
        if T == None:
            return -1
        else:
            return T.height

    def _insert(self, T, data):
        if T is None:
            T = Node(data)
        elif data < T.data:
            T.lchild = self._insert(T.lchild,data) # insert node firstly and then rotate nodes of Tree
            if (self.cal_height(T.lchild) - self.cal_height(T.rchild)) == 2:
                if data < T.lchild.data:
                    T = self.single_right_rotate(T)
                else:
                    T = self.double_right_rotate(T)

        elif data > T.data:
            T.rchild = self._insert(T.rchild,data)
            if (self.cal_height(T.lchild) - self.cal_height(T.rchild)) == -2:
                if data < T.rchild.data:
                    T = self.double_left_rotate(T)
                else:
                    T = self.single_left_rotate(T)
        T.height = max(self.cal_height(T.lchild),self.cal_height(T.rchild)) + 1
        return T

    def build_tree(self,T,data):
        for each in data:
            self.T = self.insert_node(self.T,each)

    def preorder_traverse(self, T):
        if T != None:
            print(T.data)
            self.preorder_traverse(T.lchild)
            self.preorder_traverse(T.rchild)

    def inorder_traverse(self, T):
        if T != None:
            self.inorder_traverse(T.lchild)
            print(T.data)
            self.inorder_traverse(T.rchild)

    def postorder_traverse(self, T):
        if T != None:
            self.postorder_traverse(T.lchild)
            self.postorder_traverse(T.rchild)
            print(T.data)





if __name__ == '__main__':
    data = [3,2,1,4,5,6,7,10,9,8]
    Tree = AVL()
    Tree.build_tree(Tree.T,data)
    print('one:')
    Tree.inorder_traverse(Tree.T)

    # print('\ntwo')
    # Tree.delete_node(Tree.T,47)
    # Tree.inorder_traverse(Tree.T)