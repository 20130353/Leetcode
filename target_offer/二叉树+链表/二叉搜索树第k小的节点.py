# -*- coding: utf-8 -*-
# author: sunmengxin
# time: 18-11-27
# file: 二叉搜索树第k小的节点
# description:

class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 反思：
# 1. 看到二叉搜索树就应该想到中序遍历是已经排好的顺序,中序遍历的第k个节点就是要找的节点
# 2. 我原先的想法是用后序遍历然后加二分查找,但是二分查找的效果出不来,所以就算了,应该直接想到用中序遍历的
# 3. 注意这道题返回的节点,不是节点的值!!!

class Solution:
    # 返回对应节点TreeNode

    def KthNode(self, pRoot, k):
        # write code here
        if not pRoot or k <= 0:
            return None

        stack = []
        count = 0
        cur = pRoot
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            count += 1
            if count == k:
                return cur
            cur = cur.right


if __name__ == '__main__':
    Node1 = Node(1)
    Node2 = Node(2)
    Node3 = Node(3)
    Node4 = Node(4)
    Node5 = Node(5)
    Node6 = Node(6)
    Node7 = Node(7)
    Node8 = Node(8)

    Node5.left = Node3
    Node5.right = Node7
    Node3.left = Node2
    Node3.right = Node4
    Node7.left = Node6
    Node7.right = Node8

    so = Solution()
    print(so.KthNode(Node5, 3))
