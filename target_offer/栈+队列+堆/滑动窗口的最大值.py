#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 滑动窗口的最大值.py
# @Author: smx
# @Date  : 2020/2/14
# @Desc  :

# 给定一个数组 nums，有一个大小为k的滑动窗口从数组的最左侧移动到数组的最右侧。
# 你只可以看到在滑动窗口内的 k个数字。滑动窗口每次只向右移动一位。
# 返回滑动窗口中的最大值。
# 双端队列
# 本来应该是只淘汰小的，但是是找滑动窗口内的所以要淘汰失效的
class Solution:
    def maxSlidingWindow(self, arr, k):
        win = []
        ans = []
        for i in range(len(arr)):
            # 淘汰失效的
            while win and i - win[0][1] >= k:
                win.pop(0)
            # 淘汰小的
            while win and win[-1][0] <= arr[i]:
                win.pop()
            win.append((arr[i], i))
            if i >= k - 1:
                ans.append(win[0][0])
        return ans


if __name__ == '__main__':
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 2
    # [3, 3, 5, 5, 6, 7]
    print(Solution().maxSlidingWindow(arr, k))
