#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 堆排序.py
# @Author: smx
# @Date  : 2020/2/14
# @Desc  :


# 快排
# 时间复杂度计算：单次时间n*次数logn=O(nlogn)
# 最好时间复杂度是nlogn
# 最坏是n*n
# 空间复杂度O(1)
# 不稳定排序
class QuickSort:
    def sort(self, arr, n):
        if not arr or n <= 1:
            return

        def in_sort(arr, left, right):
            if left >= right:
                return
            start, end = left, right
            key = arr[left]
            while left < right:
                while left < right and arr[right] >= key:
                    right -= 1
                if left < right:
                    arr[left] = arr[right]
                while left < right and arr[left] < key:
                    left += 1
                if left < right:
                    arr[right] = arr[left]
            arr[left] = key
            in_sort(arr, start, left - 1)
            in_sort(arr, left + 1, end)

        in_sort(arr, 0, n - 1)


# 堆排序,大根堆和小根堆,堆的性质是堆顶元素是最大的
# 核心是保证以当前节点为根的堆是有序的（大根堆或者是小根堆)
# 堆是满二叉树，
# 时间复杂度：单次时间logn*次数n=nlogn
# 最快的时间复杂度O(nlogn)
# 最坏的时间复杂度O(nlogn)
# 空间复杂度是O(1)，只有交换的时候需要占位
# 不稳定排序
class HeapSort:
    def adjust_heap(self, arr, n, father):
        while father * 2 + 1 < n:
            child = father * 2 + 1
            if child + 1 < n and arr[child + 1] > arr[child]:
                child += 1
            if arr[child] > arr[father]:
                arr[father], arr[child] = arr[child], arr[father]
                father = child
            else:
                break

    def sort(self, arr, n):
        # 建立堆
        # 从最后一个非叶子节点开始，调整以这个节点为根的堆
        # 为什么从非叶节点开始调整，因为对于叶结点没有意义
        for i in range(n // 2 - 1, -1, -1):
            self.adjust_heap(arr, n, i)
        for i in range(n - 1):
            # 拿走堆顶
            arr[0], arr[n - 1 - i] = arr[n - 1 - i], arr[0]
            # 调整堆
            self.adjust_heap(arr, n - i - 1, 0)
        return


if __name__ == '__main__':
    arr = [57, 40, 38, 11, 13, 34, 48, 75, 6, 19, 9, 7]
    # HeapSort().sort(arr, len(arr))
    QuickSort().sort(arr, len(arr))
    print(arr)
