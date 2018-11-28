# -*- coding: utf-8 -*-
# author: sunmengxin
# time: 18-11-27
# file: 二叉树的下一个节点
# description:

# 反思:
# 1. 开始没哟理解题意,不懂给定了一个节点pNode怎么找到它的下一个节点,后来懂得了要找的是这个节点的中序遍历后的第一个节点
# 这个节点可能存在的位置是后继节点或者父节点

class Solution:
    def GetNext(self, pNode):
        # write code here
        if not pNode:
            return pNode

        # 如果节点有右孩子
        if pNode.right:
            node = pNode.right
            while node.left:
                node = node.left
            return node

        # 如果节点没有右孩子
        else:
            while pNode.next:
                tmp = pNode.next
                if tmp.left == pNode:  # 找到第一个当前节点是父节点的左孩子的节点
                    return tmp
                pNode = tmp
