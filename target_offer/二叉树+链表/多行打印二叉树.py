# -*- coding: utf-8 -*-
# author: sunmengxin
# time: 18-11-25
# file: 多行打印二叉树
# description:

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return pRoot

        queue = [pRoot]
        res = []
        while queue:
            size = len(queue)
            temp = []
            while size:
                cur = queue.pop(0)
                temp.append(cur.data)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
                size -= 1
            res.append(temp)
        return res


if __name__ == '__main__':
    root = Node(1)
    Node1 = Node(1)
    Node2 = Node(2)
    Node3 = Node(3)
    Node4 = Node(4)
    Node5 = Node(5)
    Node6 = Node(6)
    Node7 = Node(7)
    root.left = Node2
    root.right = Node3
    Node2.left = Node4
    Node2.right = Node5
    Node3.left = Node6
    Node3.right = Node7


    so = Solution()
    print(so.Print(root))
