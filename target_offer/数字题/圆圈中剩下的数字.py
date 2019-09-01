# -*- coding: utf-8 -*-
# author: sunmengxin
# time: 18-11-28
# file: 圆圈中剩下的数字
# description:
# -*- coding:utf-8 -*-
# 反思:
# 一直是超时!
# 不知道为什么!
class Solution:
    def LastRemaining_Solution(self, n, m):
        # write code here

        # m 是 要报的数字
        # n 是 数组的大小
        if n < m or n <= 0 or m <= 0:
            return -1

        vis = [1 for _ in range(n)]

        i = -1
        step = 0
        count = n
        while count:
            i = (i + 1) % n
            if vis[i]:
                step += 1
                if step == m:
                    vis[i] = 0
                    count -= 1
                    step = 0
        return i


if __name__ == '__main__':
    so = Solution()
    print(so.LastRemaining_Solution(110, 10))
