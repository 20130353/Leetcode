# 容器盛水问题
# 1. 暴力做法： 每次遍历到当前节点就向左向右找到小高峰，然后计算小高峰之间的差值，时间复杂度n方
# 2. 先找到左右的小高峰，找小高峰用DP，遍历计算差值，这里不需要找小高峰，直接找最大值就好。因为最大值一定是高峰，蓄水量一定是两个高峰之间，不可能是小高峰和高峰之间
# 运行超时:您的程序未能在规定时间内运行结束，请检查是否循环有错或算法复杂度过大。
# case通过率为20.00%
# 存在的问题：时间复杂度太高了 --》 用双指针，指针每次找到最小的，用最小的顶峰-当前的体积得到盛水量！

# def solution(arr):
#     # dp(i)到节点i(包括这个节点)的左高峰
#     max_value = -float('inf')
#     left_dp = []
#     for inx in range(len(arr)):
#         left_dp.append(max_value)
#         max_value = max(arr[inx], max_value)
#
#     max_value = -float('inf')
#     right_dp = []
#     for inx in range(len(arr) - 1, -1, -1):
#         right_dp.insert(0, max_value)
#         max_value = max(arr[inx], max_value)
#
#     # print(left_dp)
#     # print(right_dp)
#     ans = 0
#     for inx in range(1, len(arr) - 1):
#         con = min(left_dp[inx], right_dp[inx]) - arr[inx]
#         if con > 0:
#             ans += con
#     return ans

def solution(arr, n):
    i, j = 0, n - 1
    max_left, max_right = arr[i], arr[j]
    ans = 0
    while i < j:
        if max_left < max_right:
            i += 1
            if arr[i] >= max_left:
                max_left = arr[i]
            else:
                ans += max_left - arr[i]
        else:
            j -= 1
            if arr[j] >= max_right:
                max_right = arr[j]
            else:
                ans += max_right - arr[j]
    return ans


if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().strip().split()))
    ans = solution(arr, n)
    print(ans)
