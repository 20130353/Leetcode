#IPO项目
from heapq import heappush, heappop, nsmallest
class Solution:

    def __init__(self):
        self.heap1 = []
        self.heap2 = []

    def find_k(self, costs, profits, k, w):
        cost_dict = {}

        for inx, each in enumerate(zip(costs, profits)):
            cost_dict[each[0]] = inx
            heappush(self.heap1, each[0])
            heappush(self.heap2, each[1])

        while k:
            while len(self.heap1) > 0 and nsmallest(1, self.heap1)[0] <= w:
                inx = cost_dict[heappop(self.heap1)]
                heappush(self.heap2, -profits[inx])

            if len(self.heap2) <= 0:
                return w
            else:
                profit = heappop(self.heap2)
                w += -profit
            k -= 1

        return w


if __name__ == '__main__':
    k, w, profits, costs = 2, 0, [1, 2, 3], [0, 1, 1]
    ans = Solution().find_k(costs, profits, k, w)
    print(ans)
