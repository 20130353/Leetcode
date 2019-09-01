# -*- coding: utf-8 -*-
# Author: sunmengxin
# time: 10/15/18
# file: 数组中出现次数超过一半的数.py
# description:

'''
    给定一个数组,求数组中出现次数超过一半的数
    解法1. 用哈希表存储每个数字出现的次数,找到出现次数最多的数字
    解法2. 出现次数最多的数字=中位数 （存在的问题是：如果是偶数个，中位数的计算很麻烦）
    解法3. 出现次数大于其他数字的出现次数的总和（但是无法确定最后一个是出现次数最多的那个数字还是第一次出现剩到最后一个了）。。。
    其他人的解决方案还是计算出了这个数字的出现次数
    解法4. import collections.Counter(numbers)
'''

# 出现次数大于其他数字的总和
class Solution:
    def MoreThanHalfNum_Solution(self,numbers):
        key_value = numbers[0]
        key_count = 1
        max_count_value = None
        max_count = 0
        for each in numbers[1:]:
            if key_count == 0:
                key_value = each
                key_count = 1
            elif each == key_value:
                key_count += 1
            elif each != key_value:
                key_count -= 1
            if max_count <= key_count:
                max_count = key_count
                max_count_value = key_value

        if max_count_value != key_value and key_count == 1:
            return 0
        else:
            return key_value


# class Solution:
#
#     # 解法一：中位数,这种方案存在的问题是一定会找到一个索引，但是不能保证是出现次数超过一般的索引，最后还得遍历一遍确定是出现次数超过一半
#     def partition(self, left, right, arr):
#
#         if left > right:
#             return left
#         key = arr[left]
#         while left < right:
#             while arr[right] >= key and left < right:
#                 right -= 1
#             if left < right:
#                 arr[left] = arr[right]
#             while arr[left] <= key and left < right:
#                 left += 1
#             if left < right:
#                 arr[right] = arr[left]
#         arr[left] = key
#         return left
#
#     def find_median(self, left, right, target, arr):
#         # write code here
#         if not arr or left > target:
#             return arr
#
#         index = self.partition(left, right, arr)
#         if index == target:
#             return index
#         elif index < target:
#             return self.find_median(index + 1, right, target, arr)
#         else:
#             return self.find_median(left, index - 1, target, arr)
#
#     def MoreThanHalfNum_Solution(self, numbers):
#         target = int(len(numbers) / 2)
#         numbers = sorted(numbers)
#         index = self.find_median(0, len(numbers)-1, target, numbers)
#         return numbers[index]



#  反思
#  1. 直接产生hashmap，fromkeys(),产生的value是None
#  2. 使用sort对map排序是lambda函数，直接输入x[1]，最后返回的是tuple数组
#  3.
# class Solution:
#     # 解法二：hasp map
#     def MoreThanHalfNum_Solution(self,numbers):
#         unique_num = {}.fromkeys(numbers)
#         for each in numbers:
#             if unique_num[each] == None:
#                 unique_num[each] = 1
#             else:
#                 unique_num[each] += 1
#         unique_num = sorted(unique_num.items(),key = lambda x:x[1],reverse=True)
#
#         if unique_num[0][1] > int(len(numbers)/2):
#             return unique_num[0][0]
#         else:
#             return 0

# 这个是hashmap的库解法
class Solution:
    def MoreThanHalfNum_Solution(self,numbers):
        import collections
        counter = collections.Counter(numbers)
        target = int(len(numbers)/2)
        counter = sorted(counter.items(),key = lambda x:x[1],reverse=True)
        if list(counter)[0][1] <= target:
            return 0
        else:
            return list(counter)[0][0]





if __name__ == '__main__':
    # data = [1,1,1,1,3,3]
    data = [1,2,3,2,2,2,5,4,2]
    data = [1,2,3,2,4,2,5,2,3]
    # [1,2,2,2,2,3,3,4,5]
    # data = [2,2,2,2,2,1,3,4,5]

    so= Solution()
    print(so.MoreThanHalfNum_Solution(data))
