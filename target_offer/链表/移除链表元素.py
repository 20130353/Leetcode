#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 移除链表元素.py
# @Author: smx
# @Date  : 2020/2/9
# @Desc  :

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeElements(self, head, val):

        if not head:
            return head

        new_head = ListNode(0xfffffff)
        new_head.next = head
        A, B = new_head, new_head.next
        while B:
            if B.val == val:
                A.next = B.next
                B = A.next
            else:
                A = A.next
                B = B.next
        return new_head.next


if __name__ == '__main__':
    arr = [0, 0, 0, 1, 2, 3, 4, 5]
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

    head = Solution().removeElements(head, 5)
    p = head
    while p:
        print(p.val)
        p = p.next
