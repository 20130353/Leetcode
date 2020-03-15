#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 合并k个有序链表.py
# @Author: smx
# @Date  : 2020/2/23
# @Desc  :


# 有以下几种解法：
# 1.逐一合并有序链表 (K*N)
# 2.分治合并有序链表-logk*N
# 3.优先队列 logN*k

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# class Solution(object):
#     # 超时！
#     def merge_two_lists(self, A, B):
#         if not A: return B
#         if not B: return A
#         head = ListNode(-1)
#         phead = head
#         while A and B:
#             if A.val <= B.val:
#                 phead.next = ListNode(A.val)
#                 phead = phead.next
#                 A = A.next
#             else:
#                 phead.next = ListNode(B.val)
#                 phead = phead.next
#                 B = B.next
#         if A:
#             phead.next = A
#         if B:
#             phead.next = B
#         return head.next
#
#     def mergeKLists(self, lists):
#         if not lists: return None
#         if len(lists) == 1: return lists[0]
#         new_head = self.merge_two_lists(lists[0], lists[1])
#         for i in range(2, len(lists)):
#             new_head = self.merge_two_lists(new_head, lists[i])
#         return new_head

# AC
class Solution(object):
    def merge_two_lists(self, A, B):
        if not A: return B
        if not B: return A
        head = ListNode(-1)
        phead = head
        while A and B:
            if A.val <= B.val:
                phead.next = ListNode(A.val)
                phead = phead.next
                A = A.next
            else:
                phead.next = ListNode(B.val)
                phead = phead.next
                B = B.next
        if A:
            phead.next = A
        if B:
            phead.next = B
        return head.next

    def mergeKLists(self, lists):
        if not lists: return None
        if len(lists) == 1: return lists[0]
        mid = len(lists) // 2
        left = self.mergeKLists(lists[:mid])
        right = self.mergeKLists(lists[mid:])
        return self.merge_two_lists(left, right)


# # 使用python的内置结构需要重写比较函数！
# # 优先队列的排序是先比较第一个，然后比较第二个！如果第二个是自定义结构就会报错！
# # 优先队列的底层是堆方法！
# # 用优先队列在python2条件下可以AC！
# class Solution(object):
#     def mergeKLists(self, lists):
#         if not list: return []
#         head = point = ListNode(0)
#         from queue import PriorityQueue
#         q = PriorityQueue()
#
#         for l in lists:
#             if l:
#                 q.put((l.val, l))
#
#         while not q.empty():
#             val, node = q.get()
#             node = node.next
#             if node:
#                 q.put((node.val, node))
#             point.next = ListNode(val)
#             point = point.next
#
#         return head.next
#
#
# # 用heapq 堆 在python2的情况下AC！
# class Solution(object):
#     def mergeKLists(self, arrs):
#
#         if not arrs: return None
#         import heapq
#         head = ListNode(-1)
#         cur = head
#         queue = []
#         for i in range(len(arrs)):
#             if arrs[i]:
#                 heapq.heappush(queue, (arrs[i].val, arrs[i]))
#         while queue:
#             val, top_node = heapq.heappop(queue)
#             save = top_node.next
#             if save:
#                 heapq.heappush(queue, (save.val, save))
#             cur.next = ListNode(val)
#             cur = cur.next
#         return head.next

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

    arr = [1, 2, 3, 4, 5, 6]
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

    arr = [1, 4, 5, 5, 6, 10]
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

    p = Solution().mergeKLists([head, head1, head2])
    while p:
        print(p.val)
        p = p.next
