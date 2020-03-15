# -*- coding: utf-8 -*-
# author: sunmengxin
# time: 18-11-25
# file: 和为s的两个数字
# description:

# 这个借用和为s的连续最大子数组最方便，时间复杂度比二分合适
class Solution:
    def binary_search(self, arr, target, left, right):
        if left > right:
            return False
        mid = (left + right) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            return self.binary_search(arr, target, mid + 1, right)
        else:
            return self.binary_search(arr, target, left, mid - 1)

        return False

    def FindNumbersWithSum(self, array, tsum):
        # write code here
        if not array or not tsum:
            return []
        for inx, each in enumerate(array):
            target = tsum - each
            if target < array[0] or target > array[-1]:
                continue
            if target >= each:
                left, right = inx, len(array) - 1
            else:
                left, right = 0, inx
            if self.binary_search(array, target, left, right):
                return [each, target]
        return []


if __name__ == '__main__':
    so = Solution()
    print(so.FindNumbersWithSum([1, 2, 3, 4, 5], 6))
