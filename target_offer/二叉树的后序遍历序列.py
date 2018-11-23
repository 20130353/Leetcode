# -*- coding: utf-8 -*-
# Author: sunmengxin
# time: 10/14/18
# file: 二叉树的后序遍历序列.py
# description:

'''
    给定一个序列,判断是否是二叉树搜索树的后序遍历
'''

# def judge(data):
#     if data == None or len(data) == 0:
#         return True
#     if len(data) == 1:
#         return True
#
#     key = data[-1]
#
#     i = 0
#     while(data[i] < key and i < len(data)-1):
#         i += 1
#
#     left = data[:i]
#     right = data[i:len(data)-1]
#
#     for each in left:
#         if each > key:
#             return False
#
#     for each in right:
#         if each < key:
#             return False
#
#     return judge(left) and judge(right)
#


class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        key = sequence[-1]
        index = -1
        index1 = -1
        for i in range(len(sequence)):
            if sequence[i] < key:
                index = i
            elif index1 == -1 and sequence[i] >= key:
                index1 = i

        if index1 > index:
            return True
        else:
            return False

if __name__ == '__main__':


    # data = []

    # data = [5,7,6,9,11,10,8]
    #
    data = [7,4,6,5]
    data = [4,8,6,12,16,14,10]

    so = Solution()

    print(so.VerifySquenceOfBST(data))

