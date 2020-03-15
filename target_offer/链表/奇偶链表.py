#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 奇偶链表.py
# @Author: smx
# @Date  : 2020/2/9
# @Desc  :

# 将奇数号排在偶数号之前，空间复杂度应为 O(1)，时间复杂度应为 O(nodes)
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def oddEvenList(self, head):
        if not head or not head.next or not head.next.next:
            return head

        A, B, C = head, head.next, head.next.next
        count = 1
        while C:
            if count == 1:
                node = ListNode(C.val)
                node.next = A.next
                A.next = node
                A = A.next
                B.next = C.next
            else:
                B = B.next
            count = 0 if count == 1 else 1
            C = C.next
        return head


if __name__ == '__main__':
    arr = [2, 1, 3, 5, 6, 4, 7]
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

    head = Solution().oddEvenList(head)
    p = head
    while p:
        print(p.val)
        p = p.next
