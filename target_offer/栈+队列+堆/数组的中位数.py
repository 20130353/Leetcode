# -*- coding: utf-8 -*-
# author: sunmengxin
# time: 18-11-27
# file: 数组的中位数
# description:


# 反思:
# 1. 可以先排序然后在找到中间位置的数字,但是存在的问题是奇数个直接就是中间的数字,但是偶数个就是中间的前面和后面,二分查找找两遍
# 2. 可以用大根堆和小跟堆来保存整个元素,保证两个堆的数目差不能超过1,这样中位数才会在两个堆的交接处
# 3. python的heapq默认是小根堆


#  from heapq import heappush,heappop,heapreplace,heappushpop
#  heappush: 把元素添加到heap中
#  heappop:把堆顶元素弹出
#  heappushpop先把元素加入到堆中然后在pop，这样比heappush在pop要快一些
#  heapreplace 先pop然后在把元素加入到堆中
#  heapify  调整堆
#  merge: 融合多个链表,进行堆调整,然后返回合并后的列表的迭代器
#  nlargest:  返回最大的n个元素
#  nsmallest: 返回最小的n个元素

class Solution:
    def __init__(self):
        self.length = 0
        self.min_heap = []
        self.max_heap = []
        self.res = []

    def Insert(self, num):
        from heapq import heappushpop, heappush, heapreplace

        self.length += 1

        # 创建大根堆和小根堆
        #  如果是偶数个元素的话,小根堆的大小不变
        if self.length % 2 == 0:
            if num > self.min_heap[0]:
                heappush(self.max_heap, -self.min_heap[0])
                heapreplace(self.min_heap, num)
            else:
                heappush(self.max_heap, -num)
        else:
            # 在小根堆中插入一个元素
            if not self.min_heap or num > self.min_heap[0]:
                heappush(self.min_heap, num)
            else:
                max_num = heappushpop(self.max_heap, -num)
                heappush(self.min_heap, -max_num)

        # 记录中位数元素
        if self.length % 2 == 0:
            # print('min\t', self.min_heap[0], '\tmax\t', self.max_heap[0])
            self.res.append((self.min_heap[0] + (-self.max_heap[0])) / 2)
        else:
            # print('min\t', self.min_heap[0])
            self.res.append(self.min_heap[0])

    def GetMedian(self,x):
        return self.res


# 最简单的写法
class Solution:
    date=[]
    def Insert(self, num):
        # write code here
        self.date.append(num)
        self.date.sort()
    def GetMedian(self,x):
        # write code here
        l=len(self.date)
        if l%2==0:
            return (self.date[l/2]+self.date[l/2-1])/2.0
        else:
            return self.date[l/2]



if __name__ == '__main__':
    # so = Solution()
    # data = [1, 2, 3, 4, 5, 6, 7]
    # [so.Insert(num) for num in data]
    # print(so.GetMedian())

    so = Solution()
    data = [5, 2, 3, 4, 1, 6, 7, 0, 8]
    [so.Insert(num) for num in data]
    print(so.GetMedian())
