# -*- coding: utf-8 -*-
# Author: sunmengxin
# time: 10/9/18
# file: 从尾到头打印链表.py
# description:

'''
输入一个链表，从尾到头打印链表每个节点的值。
这个代码写的有点麻烦！！
最后要自己写一遍自己的想法
'''
class ListNode:
    def __init__(self, x=None):
        self.val = x
        self.next = None

class Solution:
    def printListFromTailToHead(self, listNode):
        if listNode.val == None:
            return
        l = []
        head = listNode
        while head:
            l.insert(0, head.val)
            head = head.next
        return l

node1 = ListNode(10)
node2 = ListNode(11)
node3 = ListNode(13)
node1.next = node2
node2.next = node3

singleNode = ListNode(12)

test = ListNode()

S = Solution()
print(S.printListFromTailToHead(node1))
print(S.printListFromTailToHead(test))
print(S.printListFromTailToHead(singleNode))