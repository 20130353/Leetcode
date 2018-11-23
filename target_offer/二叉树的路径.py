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

class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        if not root:
            return []
        if root and not root.left and not root.right and root.val == expectNumber:
            return [[root.val]]
        res = []
        left = self.FindPath(root.left, expectNumber-root.val)
        right = self.FindPath(root.right, expectNumber-root.val)
        for i in left+right:
            res.append([root.val]+i)
        return res

if __name__ == '__main__':
    so = Solution()

    print(so.FindPath({10,5,12,4,7},22))