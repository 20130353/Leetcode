#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 分割链表.py
# @Author: smx
# @Date  : 2020/2/9
# @Desc  :


# 给定一个链表和一个特定值 x，对链表进行分隔，使得所有小于 x 的节点都在大于或等于 x 的节点之前。
# 只考虑小于的节点
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 原先也想到了双指针，但是实现的时候用有点混乱，没有想清楚直接构建两个链表
class Solution:
    def partition(self, head, x):
        new_head1 = ListNode(0xffffff)
        new_head2 = ListNode(0xffffff)

        A = new_head1  # 比它小的链表
        B = new_head2  # 比它大的链表
        C = head
        while C:
            if C.val < x:
                A.next = ListNode(C.val)
                A = A.next
            else:
                B.next = ListNode(C.val)
                B = B.next
            C = C.next
        B.next = None
        A.next = new_head2.next
        return new_head1.next


if __name__ == '__main__':
    arr = [1, 2, 4, 3, 5, 2]
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

    head = Solution().partition(head, 3)
    p = head
    while p:
        print(p.val)
        p = p.next
