#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 回文链表.py
# @Author: smx
# @Date  : 2020/2/8
# @Desc  :

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 出现的问题：
# 0. 开始没有想到在时间o(1)和空间o(n)条件下，判断是否是回文。忘记链表可以反转方向。
# 1. 测试用例的答案总是不对，最后直接提交就对了
# 2. 快慢指针的结束条件不对，结束条件直接设置成到最后一个位置或者到超出最后一个位置
# 3. 反转列表刚开始写的有问题，饭庄链表只需要两个指针
# 4. 判断回文的结束后条件写的不对，没有判断最后两个节点是否相等
class Solution:
    def isPalindrome(self, head):
        '''

        :param head: ListNode
        :return: bool
        '''
        if not head or not head.next:
            return True

        # 快慢指针找到中间
        A = head
        B = head
        while B and B.next:
            A = A.next
            B = B.next.next

        # 翻转链表
        mid = A
        B = A.next
        while B is not None:
            save = B.next
            B.next = A
            A = B
            B = save

        B = A
        A = head
        while B != mid:
            if A.val == B.val:
                A = A.next
                B = B.next
            else:
                return False
        if A == B or (A.next == B and A.val == B.val):
            return True
        return False


if __name__ == '__main__':
    # arr = []
    # arr = [1, 2, 3]
    # arr = [1, 2, 2, 1]
    # arr = [1, 2, 1]
    # arr = [1, 2]
    # arr = [1, 2, 3, 4, 3, 2, 1]

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

    ans = Solution().isPalindrome(head)
    print(ans)
