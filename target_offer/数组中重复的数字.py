# -*- coding: utf-8 -*-
# author: sunmengxin
# time: 18-11-26
# file: 数组中重复的数字
# description:

# 反思:
# 1. dict的keys()函数返回的是list,可以直接用in 和not in来判断
# 2. 单独用hash表会占用空间,所以就在原来的数组上操作

# class Solution:
#     # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
#     # 函数返回True/False
#     def duplicate(self, numbers, duplication):
#         # write code here
#         if not numbers:
#             return False
#
#         dict = {}
#         for each in numbers:
#             if each in dict.keys():
#                 duplication[0] = each
#                 return True
#             else:
#                 dict[each] = 1
#         return False

class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        if not numbers:
            return False
        n = len(numbers)
        for i in numbers:
            if numbers[i] < 0:
                duplication[0] = i + n
                return True
            numbers[i] -= n # 这里永远只会占据前面的数字的地位,不会影响后面的数字
        return False


if __name__ == '__main__':
    so = Solution()
    res = [0xfffffffff]
    print(so.duplicate([2, 3, 1, 0, 2, 5, 3], res), res)
