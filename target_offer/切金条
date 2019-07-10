
#每一次切尽可能让两边小,贪心算法
import heapq
class Solution:
    def __init__(self):

        self.heap = []

    def split_gold(self, arr):
        if not arr:
            return 0

        for each in arr:
            heapq.heappush(self.heap, each)

        res = 0
        while len(self.heap) > 1:
            d1 = heapq.heappop(self.heap)
            d2 = heapq.heappop(self.heap)
            res += d1 + d2
            heapq.heappush(self.heap, d1 + d2)
        return res


list = [10, 20]

ans = Solution().split_gold(list)
print(ans)
