# -*- coding: utf-8 -*-
# author: sunmengxin
# time: 18-11-25
# file: 两个链表的第一个公共节点
# description:


# 反思：
# 1. 使用节点next的先检查是否存在无next的情况
# 2. 返回出现错误，可能是最后的条件出现错误也有可能是开始的判断出现错误
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        if not pHead1 or not pHead2:
            return None

        stack1 = []
        cur = pHead1
        while cur:
            stack1.append(cur)
            cur = cur.next

        stack2 = []
        cur = pHead2
        while cur:
            stack2.append(cur)
            cur = cur.next

        pre = None
        while stack1 and stack2:
            top1, top2 = stack1.pop(), stack2.pop()
            if top1.val == top2.val:
                pre = top1
            else:
                break
        return pre


if __name__ == '__main__':
    so = Solution()

    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node1.next = node2
    node2.next = node3

    node = so.FindFirstCommonNode(node1, node2)

    while node:
        print(node.val, )
        node = node.next
