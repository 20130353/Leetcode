#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 合并两个有序链表.py
# @Author: smx
# @Date  : 2020/2/9
# @Desc  :

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, head1, head2):
        new_head = ListNode(0xfffff)
        new_head.next = head1
        A, B = new_head, new_head.next
        C = head2
        while B and C:
            if B.val <= C.val:
                B = B.next
                A = A.next
            else:
                node = ListNode(C.val)
                node.next = A.next
                A.next = node
                A = A.next
                C = C.next
        if C:
            A.next = C
        return new_head.next


if __name__ == '__main__':
    arr = [1]
    head1 = None
    p = None
    for inx, each in enumerate(arr):
        if inx == 0:
            head1 = ListNode(each)
            p = head1
        else:
            node = ListNode(each)
            p.next = node
            p = p.next

    arr = [2,3,4]
    head2 = None
    p = None
    for inx, each in enumerate(arr):
        if inx == 0:
            head2 = ListNode(each)
            p = head2
        else:
            node = ListNode(each)
            p.next = node
            p = p.next

    p = Solution().mergeTwoLists(head1, head2)
    while p:
        print(p.val)
        p = p.next
