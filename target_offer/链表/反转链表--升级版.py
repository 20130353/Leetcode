#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 反转链表--升级版.py
# @Author: smx
# @Date  : 2020/2/9
# @Desc  :

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 这道题比简单的反转列表多了区间控制，所以主要注意先找到区间，然后反转区间内链表，之后将反转的结果同之间的两端连接。
# 需要注意的是如果反转的左右两边，注意返回的头不同。

class Solution:
    def reverseBetween(self, head, m, n):
        if not head or m == n:
            return head

        count = 1
        p = head
        save_A = None
        save_B = p
        while count != m:
            save_A = p
            save_B = p.next
            p = p.next
            count += 1

        A = p
        B = p.next
        while count != n:
            save = B.next
            B.next = A
            A = B
            B = save
            count += 1

        if save_A:
            save_A.next = A
            save_B.next = B
            return head
        else:
            save_B.next = B
            return A


if __name__ == '__main__':
    # arr = []
    # arr = [1, 2, 3]
    # arr = [1, 2, 2, 1]
    # arr = [1, 2, 1]
    # arr = [1, 2]
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

    head = Solution().reverseBetween(head, 2, 4)
    p = head
    while p:
        print(p.val)
        p = p.next
