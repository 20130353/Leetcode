# -*- coding: utf-8 -*-
# author: sunmengxin
# time: 18-11-16
# file: 滑动窗口的最大值问题
# description:

# 反思:
# 1. 窗口初始化的问题:应该从第一个元素开始找窗口的最值,只不过是当到达第一个窗口才开始保存最值
# 2. 警惕窗口的size可能小于等于0
# 3. 改进用双端队列来做
from collections import deque


def windows_max(arr, size):
    res = []
    deq = deque()
    for i in range(len(arr)):
        # while len(deq) >= 1 and i - size >= deq[0][1]: # 这里写i-deq[0][1] < size 表示在窗口内最好！
        while len(deq) >= 1 and i - deq[0][1] < size:
            deq.popleft()
        while len(deq) >= 1 and deq[-1][0] <= arr[i]:
            deq.pop()
        deq.append((arr[i], i))
        if i >= size - 1:
            res.append(deq[0][0])
    return res


if __name__ == '__main__':
    arr = [4, 3, 5, 4, 3, 3, 6, 7]
    size = 3
    ans = windows_max(arr, size)
    print(ans)
