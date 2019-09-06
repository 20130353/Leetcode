# -*- coding: utf-8 -*-
# author: sunmengxin
# time: 18-11-27
# file: 删除链表中的重复节点
# description:

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def build_tree(self, T, val):
        if not T:
            T = ListNode(val)
        else:
            T.next = self.build_tree(T.next, val)
        return T

    def deleteDuplication(self, pHead):

        if not pHead:
            return pHead

        values = {}
        while pHead:
            if pHead.val in values.keys():
                values[pHead.val] += 1
            else:
                values[pHead.val] = 0
            pHead = pHead.next

        # print(values)
        new_head = None
        for key, value in values.items():
            if value == 0:
                new_head = self.build_tree(new_head, key)

        return new_head

    def delete_dupnodes(self, head):
        '''
        三个指针！
        :param head:
        :return:
        '''
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


if __name__ == '__main__':
    Node1 = ListNode(1)
    Node2 = ListNode(1)
    Node3 = ListNode(1)
    Node4 = ListNode(3)
    Node5 = ListNode(4)
    Node6 = ListNode(4)
    Node7 = ListNode(4)

    Node1.next = Node2
    Node2.next = Node3
    Node3.next = Node4
    Node4.next = Node5
    Node5.next = Node6

    so = Solution()
    node = so.delete_dupnodes(Node1)
    while node is not None:
        print(node.val)
        node = node.next
