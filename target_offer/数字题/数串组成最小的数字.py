# -*- coding: utf-8 -*-
# author: sunmengxin
# time: 18-11-14
# file: 数串
# description:

'''
设有n个正整数，将他们连接成一排，组成一个最大的多位整数。
如:n=3时，3个整数13,312,343,连成的最大整数为34331213。
如:n=4时,4个整数7,13,4,246连接成的最大整数为7424613。
输入描述:
有多组测试样例，每组测试样例包含两行，第一行为一个整数N（N<=100），第二行包含N个数(每个数不超过1000，空格分开)。
输出描述:
每组数据输出一个表示最大的整数。
示例1
输入
复制
2
12 123
4
7 13 4 246
输出
复制
12312
7424613
'''

'''
我写的代码只能过40%，问题出在排序上面，因为按照大小排序会导致个数较少的数字排到后面，会导致数字变小。
反思这道题本质就是按照数字的高低位排序，但是我我不知道怎么找到高低位排序。。。
'''


# import copy as cp
#
# def compare(left, right, left_index, right_index):
#     if len(right) <= right_index or left[left_index] > right[right_index]:
#         return left + right
#     elif len(left) <= left_index or left[left_index] < right[right_index]:
#         return right + left
#     else:
#         return compare(left, right, left_index + 1, right_index + 1)
#
#
# def solution(arr):
#     dict = {'1': [], '2': [], '3': [], '4': [], '5': [], '6': [], '7': [], '8': [], '9': []}
#     for each in arr:
#         num = str(each)[0]
#         dict[num].append(str(each))
#
#     for key, item in dict.items():
#         item_copy = cp.deepcopy(item)
#         item_copy = sorted(item_copy)
#         while (len(item_copy) != 1 and item_copy):
#             left = item_copy.pop()
#             right = item_copy.pop()
#             res = compare(left, right, 0, 0)
#             # print(res)
#             item_copy.append(res)
#         dict[key] = item_copy
#
#     res = ''
#     for i in range(9, 0,-1):
#         if dict[str(i)]:
#             res = res + dict[str(i)][0]
#     return res
#
#
# if __name__ == '__main__':
#     n = int(input().strip())
#     arr = list(map(int, input().strip().split(' ')))
#     # print(arr)
#     res = solution(arr)
#     print(res)
#

#   反思：
#   1. 遇到按照数字的高低位排序的问题，应该首先想到用工具自带的函数实现cmp的排序方式就可以。
# 还有这道题我既然已经想到了桶排序，那我应该可以继续想到排序的！后面想到了，但是还是没有想出来关键点，这次一定好好总结下！
#   2. string 本身就是数组，可以使用string[0]..等方式
#   3. join可以把数组连接成为一个字符串
#   4. 连接字符串最保险的方式是用+号
#   5. 这道题也犯了拿到题目就开始写的问题，想的太少了。如果是面试的时候。可以先和面试官说一下思路，问问他，他说可以的话就可以直接开始写了，如果不行的话，就继续思考。
#   6. 常用的输入输出总结下！

# 反思：
# 1. 这个compare函数可以用lambda函数实现
# 2. 对每个元素进行操作可以用map函数

class Solution:
    def PrintMinNumber(self, numbers):
        lmb = lambda n1,n2:int(str(n1)+str(n2))-int(str(n2)+str(n1))
        res = sorted(numbers, cmp=lmb)
        return ''.join(map(str,res))


# 标准代码
if __name__ == '__main__':
    so = Solution()
    print(so.PrintMinNumber([3, 32, 321]))
    print(so.PrintMinNumber([3,5,1,4,2]))
