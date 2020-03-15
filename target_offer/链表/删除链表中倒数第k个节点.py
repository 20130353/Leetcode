#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 删除链表中倒数第k个节点.py
# @Author: smx
# @Date  : 2020/2/9
# @Desc  :


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head, n):
        if not head or (not head.next and n == 1):
            return None

        new_head = ListNode(0xffff)
        new_head.next = head
        A, B = new_head, new_head
        count = 0
        while B:
            B = B.next
            if count == n + 1:
                A = A.next
            else:
                count += 1
        A.next = A.next.next
        return new_head.next


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

    p = Solution().removeNthFromEnd(head, 1)
    while p:
        print(p.val)
        p = p.next
