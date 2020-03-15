#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 删除链表节点.py
# @Author: smx
# @Date  : 2020/2/9
# @Desc  :

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 本题的题意是,存在一个我们不能直接去访问链表head,以及给定的节点node
# 我们要在无法访问head的情况下,把node节点删除
# 在面向对象的语言中,我们已知node但无法访问node的上一个节点,因此不能修改上一个节点的next属性
# 官方题解把node节点的值用下一个节点的值去覆盖掉,然后把重复值的node.next给删除掉,达成了一种"狸猫换太子"的效果

class Solution:
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next