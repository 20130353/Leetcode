import functools
# 这里就用sort来排序,避免用heapq 不能存储结构体的问题
class Meetting:
    def __init__(self, inx, start, end):
        self.inx = inx
        self.start = start
        self.end = end


class Solution:
    def sort_room(self, arr):
        sorted(arr, key=functools.cmp_to_key(lambda x, y: x.end - y.end))
        cur = 0
        count = 0
        while len(arr) > 0:
            if arr[0].end >= cur:
                top = arr.pop(0)
                cur = top.end
                count += 1
            else:
                arr.pop(0)
        return count


if __name__ == '__main__':
    arr = [[1, 1, 10],
           [2, 5, 6],
           [3, 13, 15],
           [4, 14, 17],
           [5, 8, 14],
           [6, 3, 12]]
    data = []
    for i in range(len(arr)):
        data.append(Meetting(arr[i][0], arr[i][1], arr[i][2]))
    ans = Solution().sort_room(data)
    print(ans)
