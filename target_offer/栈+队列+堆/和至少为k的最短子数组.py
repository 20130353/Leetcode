#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 和至少为k的最短子数组.py
# @Author: smx
# @Date  : 2020/2/14
# @Desc  :

from functools import cmp_to_key


# 优先队列不能随意弹出元素！遇到要修改序号的元素，需要遍历一遍然后找到元素在弹出！更加浪费时间！
# 主要浪费时间的点在map中找最近的点，可以用二分！
# 可以优化的点：查找-->二分查找！存放-->单调栈或者单调队列 ！
# 超时！
# class Solution:
#     def shortestSubarray(self, arr, K):
#         if not arr:
#             return -1
#
#         length = len(arr)
#         num = 0
#         dict = {0: -1}
#         ans = 0xfffffff
#         for i in range(length):
#             num += arr[i]
#             if num not in dict.keys() or dict[num] > i:
#                 dict[num] = i
#             target = num - K
#             items = sorted(dict.items(), key=cmp_to_key(lambda a, b: a[0] - b[0]))
#             for j in range(len(items)):
#                 if items[j][0] <= target:
#                     if i - items[j][1] < ans:
#                         ans = i - items[j][1]
#                 else:
#                     break
#         return ans if ans != 0xfffffff else -1

# 单调栈+二分查找
# 这里还可以优化的点是：前面符合要求的点可以直接删除，因为符合要求之后如果再有符合要求的，那么前面的点一定不是最优解！
# 所以优化成使用双端队列！
class Solution:
    def shortestSubarray(self, arr, K):
        if not arr:
            return -1

        length = len(arr)
        num = 0
        stack = [(0, -1)]
        ans = 0xfffffff
        for i in range(length):
            num += arr[i]
            while stack and stack[-1][0] >= num:
                stack.pop()
            stack.append((num, i))
            target = num - K  # 找到小于target的最大值
            left, right = 0, len(stack) - 1
            while left < right:
                mid = left + (right - left + 1) // 2
                if stack[mid][0] <= target:
                    left = mid
                else:
                    right = mid - 1
            if stack[left][0] <= target and i - stack[left][1] < ans:
                ans = i - stack[left][1]
        return ans if ans != 0xfffffff else -1


class Solution:
    def shortestSubarray(self, arr, K):
        import queue as Q
        if not arr:
            return -1

        length = len(arr)
        num = 0
        queue = Q.deque()
        queue.append((0, -1))
        ans = 0xfffffff
        for i in range(length):
            num += arr[i]
            while queue.__len__() > 0 and queue[-1][0] >= num:
                queue.pop()
            queue.append((num, i))
            target = num - K  # 找到小于target的最大值
            while queue.__len__() > 0 and queue[0][0] <= target:
                if i - queue[0][1] < ans: ans = i - queue[0][1]
                queue.popleft()
        return ans if ans != 0xfffffff else -1


if __name__ == '__main__':
    arr = [2, -1, 2, 4, 5, 6, 3]
    k = 12
    print(Solution().shortestSubarray(arr, k))
