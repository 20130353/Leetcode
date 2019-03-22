# -*- coding: utf-8 -*-
# author: sunmengxin
# time: 18-11-17
# file: 二叉树的路径
# description:


# class Solution:
#     # 返回二维列表，内部每个列表表示找到的路径
#
#     def find_path(self, root, sum_, path, sp, res):
#         import copy as cp
#         if not root or (not root.left and not root.right):
#             if sp == sum_:
#                 res.append(path)
#             return
#         else:
#             sp += root.val
#             path.append(root.val)
#             if root.left:
#                 self.find_path(root.left, sum_, cp.deepcopy(path), sp, res)
#             if root.right:
#                 self.find_path(root.right, sum_, cp.deepcopy(path), sp, res)
#         return
#
#     def FindPath(self, root, expectNumber):
#         # write code here
#         res = []
#         self.find_path(root, expectNumber, [], 0, res)
#         fin_res = []
#
#         for _ in len(res):
#             min_each = -1
#             for each in len(res):
#                 if min_each == -1 or len(each) < min_each:
#                     min_each = each
#             fin_res.append(min_each)
#             res.remove(min_each)
#
#         return fin_res

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


import copy


class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expect_number, res, path):
        if not root:
            return

        if sum(path) > expect_number:
            return

        if not root.left and not root.right and sum(path) == expect_number - root.val:
            path.append(root.val)
            res.append(path)
            return

        path.append(root.val)

        self.FindPath(root.left, expect_number, res, copy.deepcopy(path))

        self.FindPath(root.right, expect_number, res, copy.deepcopy(path))


if __name__ == '__main__':
    so = Solution()

    root = Node(10)
    node1 = Node(5)
    node2 = Node(12)
    node3 = Node(4)
    node4 = Node(7)

    root.left = node1
    root.right = node2
    node1.left = node3
    node1.right = node4

    res = []
    so.FindPath(root, 22, res, [])
    print(res)
