# -*- coding: utf-8 -*-
# Author: sunmengxin
# time: 10/9/18
# file: 二叉树的遍历.py
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

    def build_Tree(self, data):
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

    def delete_node(self,T,data):
        if T.data == data:
            self.delete(T,data)
        elif T.data < data:
            self.delete_node(T.rchild,data)
        else:
            self.delete_node(T.lchild,data)

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


    # # 先序遍历--栈
    # preOrder每次都将遇到的节点压入栈，当左子树遍历完毕后才从栈中弹出最后一个访问的节点，访问其右子树。
    # 在同一层中，不可能同时有两个节点压入栈，因此栈的大小空间为O(h)，h为二叉树高度。
    # 时间方面，每个节点都被压入栈一次，弹出栈一次，访问一次，复杂度为O(n)。
    def previsit_stack(self, root):
        if root == None:
            return
        stack = []
        node = root #node  相当与是指针,从根节点开始访问
        while node or stack:
            while node:
                # 从根节点开始，一直找它的左子树
                print(node.data)
                stack.append(node)
                node = node.lchild
            # while结束表示当前节点node为空，即前一个节点没有左子树了
            node = stack.pop() #从栈中弹出最后一个访问的节点,根节点
            # 开始查看它的右子树
            node = node.rchild

    # 先序和中序只是改变一下打印的位置
    def invisit_stack(self, root):
        if root == None:
            return
        stack = []
        node = root  # node  相当与是指针,从根节点开始访问
        while node or stack:
            while node:
                # 从根节点开始，一直找它的左子树
                stack.append(node)
                node = node.lchild
            # while结束表示当前节点node为空，即前一个节点没有左子树了
            node = stack.pop()  # 从栈中弹出最后一个访问的节点,根节点
            print(node.data)
            # 开始查看它的右子树
            node = node.rchild

    # 从直觉上来说，后序遍历对比中序遍历难度要增大很多。因为中序遍历节点序列有一点的连续性，
    # 而后续遍历则感觉有一定的跳跃性。先左，再右，最后才中间节点；
    # 访问左子树后，需要跳转到右子树，右子树访问完毕了再回溯至根节点并访问
    def postorder_stack(self,T):
        if T == None:
            return
        stack = [T]
        record = []
        while (len(stack) >0):
            node = stack.pop()
            record.append(node)
            if node.rchild:
                stack.append(node.rchild)
            if node.lchild:
                stack.append(node.lchild)

        for each in range(len(record)-1,0,-1):
            print(each.data)


    def level_stack(self,T):
        if T == None:
            return
        queue = [T]
        while(len(queue)>0):
            node = queue.pop()
            print(node.data)
            if node.lchild:
                queue.append(node.lchild)
            if node.rchild:
                queue.append(node.rchild)



if __name__ == '__main__':
    # data = [62,88,58,47,35,73,51,99,37,93]
    data = [62,58,88,47,73,99,35,51,93,29,37,49,56,36,48,50]
    Tree = BST()
    Tree.build_Tree(data)
    Tree.inorder_stack(Tree.T)