from heapq import heappop, heappush

# 用优先队列保存每个的最小值，每次吐出一个加入这个队列的后一个值，注意边界
def solution(arrs):
    if len(arr1) <= 0 and len(arr2 <= 0) and len(arr3) <= 0:
        return []
    queue = []
    ans = []
    for i in range(len(arrs)):
        if len(arrs[i]) > 0:
            heappush(queue, (arrs[i][0], 0, i))

    while len(queue) > 0:
        cur = heappop(queue)
        ans.append(cur[0])
        if cur[1] + 1 < len(arrs[cur[2]]):
            heappush(queue, (arrs[cur[2]][cur[1] + 1], cur[1] + 1, cur[2]))
    return ans


if __name__ == '__main__':
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [4, 5, 7, 9, 22]
    arr3 = [45, 46, 50, 60, 70, 80]

    # arr1, arr2, arr3 = [1], [2], [3]

    # arr1, arr2, arr3 = [1], [], []

    ans = solution([arr1, arr2, arr3])
    print(ans)
