# -*- coding: utf-8 -*-
# Author: sunmengxin
# time: 10/14/18
# file: 二叉搜索树和双向链表.py
# description:


'''
    给定一个二叉搜索树,要求在不使用新的节点的情况下将其改成双向链表
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

    def delete(self,T,data):
        # CN is current node with data
        # PN is the parent node of the current node
        flag,CN,PN = self.search_node(self.T,self.T,data)

        if CN.rchild == None and CN.lchild == None:
            if CN == PN.lchild:
                PN.lchild = None
            else:
                PN.rchild = None

        if CN.lchild == None and CN.rchild != None:
            if CN == PN.lchild:
                PN.lchild = CN.rchild
            else:
                PN.rchild = CN.rchild
        if CN.rchild == None and CN.lchild != None:
            if CN == PN.lchild:
                PN.lchild = CN.lchild
            else:
                PN.rchild = CN.lchild
        else:
            front_node = T.lchild
            while(front_node.rchild != None):
                front_node  = front_node.rchild

            T.data = front_node.data
            T.lchild.rchild = front_node.lchild
            del front_node
        return


def change_tree(T):
    if T == None:
        return None

    if T.lchild == None and T.rchild == None:
        return T

    left = change_tree(T.lchild)
    p = left
    while(p!= None and p.rchild != None):
        p = p.rchild

    if left != None:
        p.rchild = T
        T.lchild = p

    right = change_tree(T.rchild)
    if right != None:
        right.lchild = T
        T.rchild = right

    if left != None:
        return left
    else:
        return T

if __name__ == '__main__':

    data = [1,4,5,6,7,3,2,9]
    Tree = BST()
    Tree.build_tree(data)
    Tree = change_tree(Tree.T)
    while(Tree != None):
        print(Tree.data)
        Tree = Tree.rchild




