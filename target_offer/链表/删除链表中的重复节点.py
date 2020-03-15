#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 删除链表中的重复节点.py
# @Author: smx
# @Date  : 2020/2/9
# @Desc  :

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 出现的问题是：没有理解题意，需要保留一个重复元素
class Solution:
    def delete_dupnodes(self, head):
        new_head = ListNode(-1)
        new_head.next = head
        A = new_head
        B = new_head.next
        C = B.next

        while C != None:
            while C != None and B.val == C.val:
                C = C.next
            if B.next != C: # 就是卡在这里了！
                while B != C:
                    A.next = B.next
                    B = B.next
                if B is not None:
                    C = B.next
            else:
                A = B
                B = A.next
                C = B.next

        return new_head.next


    def deleteDuplicates(self, head):
        if not head or not head.next:
            return head

        new_head = ListNode(0xfffff)
        new_head.next = head
        C = new_head
        A = new_head.next
        B = A.next
        while A:
            if not B or A.val != B.val:
                if A.next == B:
                    C.next = A
                    C = C.next
                else:
                    C.next = ListNode(A.val)
                    C = C.next
                A = B
            if B:
                B = B.next
        C.next = A
        return new_head.next


if __name__ == '__main__':
    arr = [1, 1, 2]
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

    p = Solution().deleteDuplicates(head)
    while p:
        print(p.val)
        p = p.next
