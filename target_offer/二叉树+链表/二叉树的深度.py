# -*- coding: utf-8 -*-
# Author: sunmengxin
# time: 10/20/18
# file: 二叉树的深度.py
# description:

'''
    求二叉树的深度有两种解法:
    递归: 返回左右节点的最大深度 + 当前深度1
    非递归: 用二叉树的层次遍历,返回深度
'''


# 反思：
# 1. list的pop是可以接受参数
# 默认的list.pop() == list.pop(-1)
# 如果想要删除的是第一个用 list.pop(0)

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 递归的方式
    def TreeDepth(self, pRoot):
        # write code here
        if not pRoot:
            return 0
        else:
            return max(self.TreeDepth(pRoot.left), self.TreeDepth(pRoot.right)) + 1

    # 栈的方式
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
    max_deepth = so.Stack_TreeDepth(root)
    print(max_deepth)
