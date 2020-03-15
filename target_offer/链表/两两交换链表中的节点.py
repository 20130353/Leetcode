#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 两两交换链表中的节点.py
# @Author: smx
# @Date  : 2020/2/9
# @Desc  :

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head):
        if not head or not head.next:
            return head
        flag = 1
        A, B = head, head.next
        while A and B:
            if flag == 1:
                temp = B.val
                B.val = A.val
                A.val = temp
                flag = 0
                A = A.next
                B = B.next
            else:
                A = A.next
                B = B.next
                flag = 1
        return head


if __name__ == '__main__':
    arr = [1]
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

    p = Solution().swapPairs(head)
    while p:
        print(p.val)
        p = p.next
