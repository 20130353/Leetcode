#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 重排链表.py
# @Author: smx
# @Date  : 2020/2/10
# @Desc  :

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def split(self, head):

        if not head or not head.next:
            return head
        if not head.next.next:
            save = head.next
            head.next = None
            return head, save

        fast, slow = head, head
        while fast.next:
            slow = slow.next
            fast = fast.next
            if fast.next: fast = fast.next
        save = slow.next
        slow.next = None
        return head, save

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

    def reorderList(self, head):
        if not head or not head.next:
            return

        head1, head2 = self.split(head)
        reverse_head2 = self.reverseList(head2)
        A, B = head1, reverse_head2
        while A and B:
            node = ListNode(B.val)
            B = B.next
            node.next = A.next
            A.next = node
            A = A.next.next
        head = head1


if __name__ == '__main__':
    arr = [1, 2, 3]
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

    p = Solution().reorderList(head)
    while p:
        print(p.val)
        p = p.next
