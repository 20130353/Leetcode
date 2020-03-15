#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 排序链表.py
# @Author: smx
# @Date  : 2020/2/9
# @Desc  :

# 如果用插入排序超时！
# 改成归并排序，使用快慢指针将链表分成两部分，对两部分分别排序之后合并
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

    def merge(self, head1, head2):
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

    def sortList(self, head):
        if not head or not head.next:
            return head
        head1, head2 = self.split(head)
        new_head1 = self.sortList(head1)
        new_head2 = self.sortList(head2)
        head = self.merge(new_head1, new_head2)
        return head


if __name__ == '__main__':
    arr = [4,3]
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

    p = Solution().sortList(head)
    while p:
        print(p.val)
        p = p.next
