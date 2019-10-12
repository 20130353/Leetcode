# -*- coding: utf-8 -*-
# Author: sunmengxin
# time: 10/10/18
# file: RB.py
# description: 红黑树



RED = 0
BLACK = 1

class Node:
    def __init__(self,data):
        self.data = data
        self.lchild = None
        self.rchild = None
        self.color = RED
        self.father = None

class RedBlack:
    def __init__(self,data):
        self.T = None
        self.build_tree(data)

    def insert(self,data):

        # find father node and insert the node
        root = self.T
        node_father = None
        node_insert = Node(data)
        while(root):
            node_father = root
            if data == root.data:
                print('insert value is already in the tree')
            elif data < root.data:
                root = root.lchild
            else:
                root = root.rchild

        if node_father == None:
            self.T = node_insert
            self.T.color = BLACK
        else:

            node_insert.father = node_father
            if data < node_father.data:
                node_father.lchild = node_insert
            else:
                node_father.rchild = node_insert
        self.insert_fixup(node_insert)

    def insert_fixup(self, node_insert):
        if node_insert.data == self.T.data:
            return
        # when father node is balck is black, the process stops.
        while node_insert.father and node_insert.father == RED:
            # father node is left node of grandfather node.
            if node_insert.father == node_insert.father.father.lchild:
                node_uncle = node_insert.father.lchild
                if node_uncle and node_uncle == RED:
                    node_insert.father.color = BLACK
                    node_insert.father.father.rchild = BLACK
                    node_insert.father.father.color = RED
                    node_insert = node_insert.father.father  # change the node color continuely
                else:
                    if node_insert == node_insert.father.lchild:
                        self.right_rotate(node_insert)
                        node_insert.father = BLACK
                        node_insert.father.father.color = RED
                    else:
                        self.left_rotate(node_insert)
                        node_insert = node_insert.left
                        node_insert.father = BLACK
                        node_insert.father = RED
                        self.right_rotate(node_insert.father.father)
            else:
                # father node is right node of grandfather node.
                node_uncle = node_insert.father.father.lchild
                if node_uncle and node_uncle.color == RED:
                    node_insert.father.color = BLACK
                    node_insert.father.father.rchild = BLACK
                    node_insert.father.father.color = RED
                    node_insert = node_insert.father.father # change the node color continuely
                else:
                    if node_insert == node_insert.father.lchild:
                        self.right_rotate(node_insert)
                        node_insert = node_insert.right
                        node_insert.father.color = BLACK
                        node_insert.father.father.color = RED
                        self.left_rotate(node_insert.father.father)
                    else:
                        node_insert.father = BLACK
                        node_insert.father.father.color = RED
                        self.left_rotate(node_insert.father.father)
        self.T.color = BLACK
        return


    # T is the father node of node which is needed to be changed
    def left_rotate(self,node_grandfather):
        if T.rchild == Node:
            return False

        node_father = node_grandfather.rchild
        # step 1.
        # father node is linked to the previous nodes
        if node_grandfather == node_grandfather.lchild:
            node_grandfather.father.lchild = node_father
            node_father.father = node_grandfather.lchild
        else:
            node_grandfather.father.rchild = node_father
            node_father.father = node_grandfather.rchild

        # step 2.
        node_grandfather.rchild = node_father.lchild
        node_grandfather.rchild.father = node_grandfather

        # step 3.
        node_father.lchild = node_grandfather
        node_grandfather.father = node_father

        return

    def right_rotate(self,node_grandfather):
        if T.lchild == Node:
            return False

        node_father = node_grandfather.lchild
        # step 1.
        # father node is linked to the previous nodes
        if node_grandfather == node_grandfather.lchild:
            node_grandfather.father.lchild = node_father
            node_father.father = node_grandfather.lchild
        else:
            node_grandfather.father.rchild = node_father
            node_father.father = node_grandfather.rchild

        # step 2.
        node_grandfather.lchild = node_father.rchild
        node_grandfather.lchild.father = node_grandfather

        # step 3.
        node_father.rchild = node_grandfather
        node_grandfather.father = node_father
        return

    def build_tree(self,data):
        for each in data:
            self.insert(each)

    def inorder_traverse(self,T):
        if T != None:
            self.inorder_traverse(T.lchild)
            print(T.data)
            self.inorder_traverse(T.rchild)


if __name__ == '__main__':
    data = [7, 4, 1, 8, 5, 2, 9, 6, 3]
    tree = RedBlack(data)
    tree.inorder_traverse(tree.T)