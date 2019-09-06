# -*- coding: utf-8 -*-
# Author: sunmengxin
# time: 10/14/18
# file: 二叉搜索树的后序遍历序列.py
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

# class Solution:
#     # 这种方法不能完全判断子串也是二叉排序树的后序遍历,上面的第一种方法才能判断
#     def VerifySquenceOfBST(self, sequence):
#         key = sequence[-1]
#         index = -1
#         index1 = -1
#         for i in range(len(sequence)):
#             if sequence[i] < key:
#                 index = i
#             elif index1 == -1 and sequence[i] >= key:
#                 index1 = i
#         # 这个方法有问题！因为这只保证当前字符串是后序，但是不能保证其子字符串也是后序
#         if index1 > index:
#             return True
#         else:
#             return False


class Solution:
    def VerifySquenceOfBST(self, arr, **dict):
        n = len(arr)
        if arr is None or n == 0:
            return False

        if n == 1:
            return True

        key = arr[-1]
        j = n - 2
        while arr[j] > key and j >= 0:
            j -= 1
        mid = j + 1
        while arr[j] < key and j >= 0:
            j -= 1
        if j >= 0:
            return False

        ans = True
        left = arr[:mid]
        left_n = len(left)
        if left_n > 0:
            ans &= self.VerifySquenceOfBST(left)

        right = arr[mid:n - 1]
        right_n = len(right)
        if right_n > 0:
            ans &= self.VerifySquenceOfBST(right)
        return ans


if __name__ == '__main__':
    # data = []
    data = [5, 7, 6, 9, 11, 10, 8]
    # data = [7, 4, 6, 5]
    # data = [4, 8, 6, 12, 16, 14, 10]
    ans = Solution().VerifySquenceOfBST(data)
    print(ans)
