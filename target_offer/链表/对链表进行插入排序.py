#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 对链表进行插入排序.py
# @Author: smx
# @Date  : 2020/2/9
# @Desc  :

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def insert(self, head, val):
        if not head:
            head = ListNode(val)
            return head
        new_head = ListNode(0xffff)
        new_head.next = head
        A, B = new_head, new_head.next
        while B and B.val <= val:
            A = A.next
            B = B.next
        if not B:
            A.next = ListNode(val)
        else:
            node = ListNode(val)
            node.next = A.next
            A.next = node
        return new_head.next

    def insertionSortList(self, head):
        if not head or not head.next:
            return head
        A = head
        new_head = None
        while A:
            new_head = self.insert(new_head, A.val)
            A = A.next
        return new_head


if __name__ == '__main__':
    arr = [4, 3, 5, 2, 7]
    head = None
    p = None
    for inx, each in enumerate(arr):
        if inx == 0:
            head = ListNode(each)
            p = head
        else:
            node = ListNode(each)
            p.next = node
            p = p.next

    p = Solution().insertionSortList(head)
    while p:
        print(p.val)
        p = p.next
