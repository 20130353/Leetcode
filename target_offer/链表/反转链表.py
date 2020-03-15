#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 反转链表.py
# @Author: smx
# @Date  : 2020/2/8
# @Desc  :

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head):
        if not head or not head.next:
            return head

        A = head
        B = head.next
        while B:
            save = B.next
            B.next = A
            if A == head:
                A.next = None
            A = B
            B = save
        return A


if __name__ == '__main__':
    # arr = []
    # arr = [1, 2, 3]
    # arr = [1, 2, 2, 1]
    # arr = [1, 2, 1]
    # arr = [1, 2]
    arr = [1,2,3,4,5,6,7]

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

    head = Solution().reverseList(head)
    p = head
    while p:
        print(p.val)
        p = p.next
