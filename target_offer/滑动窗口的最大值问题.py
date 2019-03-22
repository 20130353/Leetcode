# -*- coding: utf-8 -*-
# author: sunmengxin
# time: 18-11-16
# file: 滑动窗口的最大值问题
# description:

# 反思:
# 1. 窗口初始化的问题:应该从第一个元素开始找窗口的最值,只不过是当到达第一个窗口才开始保存最值
# 2. 警惕窗口的size可能小于等于0

class Solution:
    def maxInWindows(self, num, size):

        if not num or size <= 0:
            return []

        if size == 1:
            return num

        queue = []
        #init
        queue.append((max(num[:size]),num.index(max(num[:size]))))
        res = []

        # 判断后续的窗口最值
        for i in range(len(num)):

            # 判断queue的头元素是否还在窗口中,如果不在就一直弹出
            while(queue and queue[0][1] <= i- size):
                queue.pop(0)

            # 队列为空
            if not queue:
                queue.append((num[i],i))
            else:
                # 队列不为空
                if num[i] >= queue[0][0]:
                    del queue[:]
                    queue.append((num[i], i))
                else:
                    while (queue[-1][0] <= num[i]):
                        queue.pop()
                    queue.append((num[i], i))

            if i >= size-1:
                res.append(queue[0][0])

        return res

if __name__ == '__main__':
    so = Solution()
    # print(so.maxInWindows([2,3,4,2,6,2,5,1],3))
    print(so.maxInWindows([16,14,12,10,8,6,4],5))


