from collections import deque
def max_min_subarr(arr, num):
    max_deq = deque()
    min_deq = deque()
    ans = 0
    j = 0
    for i in range(len(arr)):
        flag = 0
        while j < len(arr):
            while len(max_deq) >= 1 and max_deq[0][1] < i:
                max_deq.popleft()
            while len(max_deq) >= 1 and max_deq[-1][0] <= arr[j]:
                max_deq.pop()
            max_deq.append((arr[j], j))

            while len(min_deq) >= 1 and min_deq[0][1] < i:
                min_deq.popleft()
            while len(min_deq) >= 1 and min_deq[-1][0] >= arr[j]:
                min_deq.pop()
            min_deq.append((arr[j], j))

            if max_deq[0][0] - min_deq[0][0] > num:
                flag = 1
                ans += j - i
                break
            else:
                j += 1
        if flag == 0:
            ans += j - i
    return ans

# 用滑动窗口的时间复杂度可以降为O(N), 之前是O(N^2)
if __name__ == '__main__':
    arr = [4, 3, 5, 4, 3, 3, 6, 7]
    ans = max_min_subarr(arr, 10)
    print(ans)
