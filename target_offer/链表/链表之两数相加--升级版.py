#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 链表之两数相加.py
# @Author: smx
# @Date  : 2020/2/9
# @Desc  :

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 这道题是升级版，需要将链表进行反转，链表顺序相加,结果进行反转！

class Solution:
    def reversedList(self, head):
        if not head or not head.next:
            return head

        A, B = head, head.next
        while B:
            save = B.next
            B.next = A
            if A == head:
                A.next = None
            A = B
            B = save
        return A

    def add(self, head1, head2):
        A, B = head1, head2
        head, C = None, None
        flag = 0
        while A or B or flag:
            num = 0
            if flag:
                num += 1
                flag = 0
            if A:
                num += A.val
                A = A.next
            if B:
                num += B.val
                B = B.next
            if num >= 10:
                flag = 1
                num -= 10
            if C is None:
                C = ListNode(num)
                head = C
            else:
                C.next = ListNode(num)
                C = C.next
        return head

    def addTwoNumbers(self, head1, head2):

        new1 = self.reversedList(head1)
        new2 = self.reversedList(head2)
        sum_list = self.add(new1, new2)
        reversed_list = self.reversedList(sum_list)
        return reversed_list


if __name__ == '__main__':
    arr = [0]
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

    arr = [1, 7]
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

    head = Solution().addTwoNumbers(head1, head2)
    p = head
    while p:
        print(p.val)
        p = p.next
