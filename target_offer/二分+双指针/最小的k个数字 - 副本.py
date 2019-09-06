# -*- coding: utf-8 -*-
# author: sunmengxin
# time: 18-11-23
# file: 最小的k个数字
# description:

# 反思：
# 1. 判断条件：left>right,不要写成left<right这种了
# 2. 判断给定的k是否大于整个数组的长度

class Solution:
    def partition(self, left, right, arr):
        if left > right:
            return left
        key = arr[left]
        while left < right:
            while arr[right] >= key and left < right:
                right -= 1
            if left < right:
                arr[left] = arr[right]
            while arr[left] <= key and left < right:
                left += 1
            if left < right:
                arr[right] = arr[left]
        arr[left] = key
        return left

    def find_k(self, left, right, arr, k):
        index = self.partition(left, right, arr)
        if index == k:
            return arr[:k]
        elif index < k:
            return self.find_k(index + 1, right, arr, k)
        else:
            return self.find_k(left, index - 1, arr, k)

    def GetLeastNumbers_Solution(self, tinput, k):
        if not tinput:
            return tinput
        if k <= 0 or k > len(tinput):
            return []
        return sorted(self.find_k(0, len(tinput) - 1, tinput, k))

if __name__ == '__main__':
    so = Solution()
    print(so.GetLeastNumbers_Solution([4,5,1,6,2,7,3,8],4))