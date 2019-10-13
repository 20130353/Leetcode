# -*- coding: utf-8 -*-
# Author: sunmengxin
# time: 10/10/18
# file: 小矩形覆盖大矩形.py
# description:

class Solution:
    def rectCover(self, n):
        if n < 0:
            return 0

        a = [0, 1, 2]
        for i in range(3, n + 1):
            a.append(a[i - 1] + a[i - 2])
        return a[n]


if __name__ == '__main__':
    ans = Solution().rectCover(1)
    print(ans)
