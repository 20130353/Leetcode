#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 链表.py
# @Author: smx
# @Date  : 2020/2/14
# @Desc  :

# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 重排链表.py
# @Author: smx
# @Date  : 2020/2/10
# @Desc  :

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 将后n个插入前n个
class Solution:
    # 分割操作：将链表分成相等的两部分。
    # 需要加入新的头结点
    def split(self, head):
        # 第一步判断是否是空节点
        if not head or not head.next:
            return head

        new_head = ListNode(0xfffffff)
        new_head.next = head

        # 用快慢指针遍历到最后一个节点，
        # 快指针到最后一个节点的时候，慢指针指向中间节点或者中间的后前一个节点
        fast, slow = new_head, new_head
        while fast.next:
            slow = slow.next
            fast = fast.next
            if fast.next: fast = fast.next
        save = slow.next
        slow.next = None
        return new_head.next, save

    # 反转操作
    # 不需要加入新的头结点
    def reverseList(self, head):
        if not head or not head.next:
            return head

        A = head
        B = head.next
        # 一前一后，保存后的后面元素，将后指针的尾连接到前，同时后移
        while B:
            save = B.next
            B.next = A
            if A == head:
                A.next = None
            A = B
            B = save
        return A

    # 插入操作
    # 本来需要插入头结点，但是这里明确了就不需要插入头结点！
    def reorderList(self, head):
        if not head or not head.next:
            return

        head1, head2 = self.split(head)
        reverse_head2 = self.reverseList(head2)
        A, B = head1, reverse_head2
        # 插入节点的步骤：新建元素，先保存后的元素，保存的元素接到插入节点的后面，将插入节点连接之前的节点
        while A and B:
            node = ListNode(B.val)
            B = B.next
            node.next = A.next
            A.next = node
            A = A.next.next
        return head1


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
