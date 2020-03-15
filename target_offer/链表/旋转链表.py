#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 旋转链表.py
# @Author: smx
# @Date  : 2020/2/10
# @Desc  :

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 这种做法存在问题：当k>链表的长度，结果就错了，所以只能按照题目要求将每次把最后一个插入到第一个，计数
# 这个做法超时！所以就先计算长度，将余数转一下
class Solution:

    def getLen(self, head):
        A = head
        count = 0
        while A:
            A = A.next
            count += 1
        return count

    def rotateRight(self, head, n):
        if not head or not head.next or n == 0:
            return head

        length = self.getLen(head)
        if n >= length:
            n = n % length
        count = 0
        while count < n:
            A = head
            B = head.next
            while B.next:
                A = A.next
                B = B.next
            A.next = None
            node = ListNode(B.val)
            node.next = head
            head = node
            count += 1
        return head


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]
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

    p = Solution().rotateRight(head, 2)
    while p:
        print(p.val)
        p = p.next
