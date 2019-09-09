# -*- coding:utf-8 -*-
class Solution:
    def merge(self, left, right, count):
        arr = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr.append(left[i])
                i += 1
            else:
                count[0] += len(left) - i
                arr.append(right[j])
                j += 1
        if i != len(left):
            # count[0] += len(left) - i
            arr += left[i:]
        if j != len(right):
            arr += right[j:]
        return arr

    def merge_sort(self, arr, count):

        if len(arr) <= 1:
            return arr

        if len(arr) == 2:
            if arr[0] > arr[1]:
                count[0] += 1
                return arr[-1::-1]
            else:
                return arr

        left = self.merge_sort(arr[:len(arr) // 2], count)
        right = self.merge_sort(arr[len(arr) // 2:], count)
        arr = self.merge(left, right, count)
        return arr

    def InversePairs(self, data):
        count = [0]
        self.merge_sort(data, count)
        return count[0] % (1000000007)
