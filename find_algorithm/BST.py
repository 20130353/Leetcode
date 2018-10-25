# -*- coding: utf-8 -*-
# Author: sunmengxin
# time: 10/8/18
# file: BST.py
# description: binary search tree

import numpy as np

class Node:
    def __init__(self,data):
        self.data = data
        self.lchild = None
        self.rchild = None

class BST:
    def __init__(self):
        self.T = None

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

    def delete(self,T,data):

        # 找到当前节点的位置和节点的父亲
        father = T
        current = T
        is_left = False
        while current.data != data:
            father = current
            if data < current.data:
                is_left = True
                current = current.lchild
            else:
                is_left = False
                current = current.rchild
            if current == None:
                return current

        # 叶子节点--直接删除
        if current.rchild == None and current.lchild == None:
            if is_left:
                father.lchild = None
            else:
                father.rchild = None

        # 只有右节点--把右节点的值给父节点
        elif current.lchild == None and current.rchild != None:
            # 是父亲的的左节点
            if is_left:
                father.lchild = current.rchild
            else:
                father.rchild = current.rchild

        #  只有左节点--把左节点的值给父节点
        elif current.rchild == None and current.lchild != None:
            # 是父亲的左节点
            if is_left:
                father.lchild = father.lchild
            else:
                father.rchild = current.lchild
        else:
            # 有两个孩子
            # 找到删除节点的前驱节点(就是删除节点中数值最大的节点)
            successor = self.get_succesor(current)
            successor.lchild = current.lchild # 后继节点的左节点是被删除节点的左节点
            current = successor

        return current

    #
    # def get_predecessor(self,delete_node):
    #     predecessor = None
    #     predecessor_father = None
    #     current = delete_node.left
    #     while current != None:
    #         predecessor_father = predecessor
    #         predecessor = current
    #         current = current.rchild
    #
    #     # 后继节点把被删除节点的右节点接起来
    #     if predecessor != delete_node.lchild:
    #         predecessor_father.rchild = predecessor.lchild
    #         predecessor.lchild = delete_node.lchild
    #
    #     return predecessor



    def get_succesor(self,delete_node):
        successor = None
        successor_father = None
        current = delete_node.rchild
        while current != None:
            successor_father = successor
            successor = current
            current = current.lchild

        if successor != delete_node.rchild:
            successor_father.lchild = successor.rchild
            successor.rchild = delete_node.rchild

        return successor

    def delete_node(self,T,data):
        if T.data == data:
            T = self.delete(T,data)
        elif T.data < data:
            T.rchild = self.delete_node(T.rchild,data)
        else:
            T.lchild = self.delete_node(T.lchild,data)
        return T

    def preorder_traverse(self,T):
        if T != None:
            print(T.data)
            self.preorder_traverse(T.lchild)
            self.preorder_traverse(T.rchild)

    def inorder_traverse(self,T):
        if T != None:
            self.inorder_traverse(T.lchild)
            print(T.data,end='\t')
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
    print('one:')
    Tree.inorder_traverse(Tree.T)

    print('\ntwo')
    T = Tree.delete_node(Tree.T,47)
    Tree.inorder_traverse(T)