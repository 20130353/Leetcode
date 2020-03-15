# -*- coding: utf-8 -*-
# Author: sunmengxin
# time: 10/10/18
# file: 重建二叉树.py
# description:

'''
 给出二叉树是前序遍历和中序遍历，求二叉树的后序遍历
'''

class Node:
    def __init__(self,data):
        self.data = data
        self.rchild = None
        self.lchild = None


# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 这是牛客网AC的代码
# 出现的问题是调用函数没有使用self
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if len(pre) == 0 or len(tin) == 0 or pre == None or tin == None:
            return None

        root_value = pre[0]
        index = tin.index(root_value)
        tin_left = tin[:index]
        tin_right = tin[index + 1:]
        left_length = len(tin[:index])
        pre_left = pre[1:left_length + 1]
        pre_right = pre[left_length + 1:]

        root_node = TreeNode(root_value)
        root_node.left = self.reConstructBinaryTree(pre_left, tin_left)
        root_node.right = self.reConstructBinaryTree(pre_right, tin_right)

        return root_node


def build_tree(predata,indata):

    if len(predata) != len(indata):
        return None

    if predata == Node or len(predata) == 0:
        return None

    if len(predata) == 1:
        return Node(predata[0])

    T = Node(predata[0])
    inx = indata.index(predata[0])

    sub_indata = indata[:inx]
    sub_predata = predata[1:len(sub_indata) + 1]
    T.lchild = build_tree(sub_predata, sub_indata)

    sub_indata = indata[inx + 1:]
    sub_predata = predata[len(sub_indata):]
    T.rchild = build_tree(sub_predata, sub_indata)

    return T


def post_track(T):
    if T != None:
        post_track(T.lchild)
        post_track(T.rchild)
        print(T.data)

if __name__ == '__main__':
    predata = [1,2,4,7,3,5,6,8]
    indata = [4,7,2,1,5,3,8,6]
    T = build_tree(predata,indata)
    post_track(T)