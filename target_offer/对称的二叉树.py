# -*- coding: utf-8 -*-
# Author: sunmengxin
# time: 10/19/18
# file: 对称的二叉树.py
# description:
'''
    对称的二叉树就是判断二叉树是否和二叉树的镜像相同,如果相同就是对称二叉树,如果不相同就不是对称二叉树
'''


class Node:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None

# 反思:
# 1. 出现的问题是改变树的左右节点时,会影响树本身的节点,所以最好在传递参数的时候用复制的方式
class Solution:

    def is_same(self, r1, r2):

        # 两个都是空
        if not r1 and not r2:
            return True
        # 一个是空,另一个不是空
        if (r1 and not r2) or (r2 and not r1):
            return False

        # 两个都不是空
        if r1.val == r2.val:
            return self.is_same(r1.left, r2.left) and self.is_same(r1.right, r2.right)
        else:
            return False

    def mirror_tree(self, pRoot):

        if not pRoot:
            return pRoot

        pRoot.left, pRoot.right = pRoot.right, pRoot.left
        pRoot.left = self.mirror_tree(pRoot.left)
        pRoot.right = self.mirror_tree(pRoot.right)
        return pRoot

    def isSymmetrical(self, pRoot):

        import copy as cp
        if not pRoot:
            return True
        mirror_tree = self.mirror_tree(cp.deepcopy(pRoot))
        return self.is_same(pRoot, mirror_tree)


if __name__ == '__main__':
    root = Node(8)
    Node1 = Node(6)
    Node2 = Node(9)
    Node3 = Node(5)
    Node4 = Node(7)
    Node5 = Node(7)
    Node6 = Node(5)


    root.left = Node1
    root.right = Node2
    Node1.left = Node3
    Node1.right = Node4
    Node2.left = Node5
    Node2.right = Node6
    #
    # res = judge_tree(root,root)
    # if res:
    #     print('Yes')
    # else:
    #     print('No')

    # root = Node(10)
    # Node11 = Node(11)
    # root.left = Node11
    # root.right = Node11

    so = Solution()
    res = so.isSymmetrical(root)
    if res:
        print('Yes')
    else:
        print('No')
