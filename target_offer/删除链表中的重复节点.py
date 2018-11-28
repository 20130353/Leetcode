# -*- coding: utf-8 -*-
# author: sunmengxin
# time: 18-11-27
# file: 删除链表中的重复节点
# description:

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    def build_tree(self, T, val):
        if not T:
            T = ListNode(val)
        else:
            T.next = self.build_tree(T.next, val)
        return T

    def deleteDuplication(self, pHead):

        if not pHead:
            return pHead

        values = {}
        while pHead:
            if pHead.val in values.keys():
                values[pHead.val] += 1
            else:
                values[pHead.val] = 0
            pHead = pHead.next

        # print(values)
        new_head = None
        for key, value in values.items():
            if value == 0:
                new_head = self.build_tree(new_head, key)

        return new_head

if __name__ == '__main__':
    Node1 = ListNode(1)
    Node2 = ListNode(1)
    Node3 = ListNode(1)
    Node4 = ListNode(3)
    Node5 = ListNode(4)
    Node6 = ListNode(4)
    Node7 = ListNode(4)

    Node1.next = Node2
    Node2.next = Node3

    node = Node1
    while node:
        print(node.val)
        node = node.next

    so = Solution()
    node = so.deleteDuplication(Node1)
    print('----------res:')
    while node:
        print(node.val)
        node = node.next
