# -*- coding: utf-8 -*-
# author: sunmengxin
# time: 18-11-25
# file: 判断是否是平衡二叉树
# description:


# 反思：空树是平衡二叉树
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def Stack_TreeDepth(self, pRoot):
        if not pRoot:
            return 0
        queue = [pRoot]
        count = 0
        while queue:
            size = len(queue)
            count += 1
            # print(count, size)
            while size:
                cur = queue.pop(0)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
                size -= 1
        return count


    def IsBalanced_Solution(self, pRoot):
        if not pRoot:
            return False
        left_height = self.Stack_TreeDepth(pRoot.left)
        right_height = self.Stack_TreeDepth(pRoot.right)
        if abs(left_height - right_height) <= 1:
            return True
        else:
            return False


if __name__ == '__main__':
    root = TreeNode(0)
    Node1 = TreeNode(1)
    Node2 = TreeNode(2)
    Node3 = TreeNode(3)
    Node4 = TreeNode(4)
    Node5 = TreeNode(5)
    Node6 = TreeNode(6)
    Node7 = TreeNode(7)
    root.left = Node2
    root.right = Node3
    Node2.left = Node4
    Node2.right = Node5
    Node3.left = Node6
    Node3.right = Node7

    so = Solution()
    max_deepth = so.IsBalanced_Solution(root)
    print(max_deepth)

