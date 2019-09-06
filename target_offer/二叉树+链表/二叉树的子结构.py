# -*- coding: utf-8 -*-
# author: sunmengxin
# time: 18-11-28
# file: 二叉树的子结构
# description:

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# class Solution:
#
#     def is_same(self, root1, root2):
#         # 返回True/False
#         if root1 and not root2:
#             return True
#         elif not root1 and root2:
#             return False
#         elif not root1 and not root2:
#             return True
#
#         if root1.val == root2.val:
#             return self.is_same(root1.left, root2.left) and self.is_same(root1.right, root2.right)
#         else:
#             return False
#
#     def HasSubtree(self, pRoot1, pRoot2):
#         # write code here
#         if not pRoot1 or not pRoot2:
#             return False
#
#         if pRoot1.val == pRoot2.val:
#             if self.is_same(pRoot1.left, pRoot2.left) and self.is_same(pRoot1.right, pRoot2.right):
#                 return True
#             else:
#                 return self.HasSubtree(pRoot1.left, pRoot2) or self.HasSubtree(pRoot1.right, pRoot2)
#         else:
#             return self.HasSubtree(pRoot1.left, pRoot2) or self.HasSubtree(pRoot1.right, pRoot2)
#


class Node:
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None
#
# def search_root(T, data):
#     if T == None:
#         return False
#     if T.data == data:
#         return T, None
#     return
#
#
# def AhasB(A, B):
#     if B == None:
#         return True
#     if A == None:
#         return False
#     if A.data != B.data:
#         return False
#     return AhasB(A.lchild, B.lchild) and AhasB(A.rchild, B.rchild)
#
#
# def judge(A, B):
#     result = False
#     if A != None and B != None:
#         if A.data == B.data:
#             result = AhasB(A, B)
#         if result == False:
#             result = judge(A.lchild, B)
#         if result == False:
#             result = judge(A.rchild, B)
#     return result

def AhasB(A, B):
    if A is None and B is None:
        return True

    if A is None or B is None:
        return False

    if A.data == B.data:
        return AhasB(A.lchild,B.rchild) and AhasB(A.rchild,B.rchild)
    else:
        return False


def judge(A, B):
    if A is None and B is None:
        return True
    if A is None or B is None:
        return False
    if A.data == B.data:
        if AhasB(A, B):
            return True
        else:
            return judge(A.lchild, B) or judge(A.rchild, B)