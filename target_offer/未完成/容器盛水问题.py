# 容器盛水问题

# 1. 暴力做法： 每次遍历到当前节点就向左向右找到小高峰，然后计算小高峰之间的差值，时间复杂度n方
# 2. 先找到左右的小高峰，找小高峰用DP，遍历计算差值，这里不需要找小高峰，直接找最大值就好。因为最大值一定是高峰，蓄水量一定是两个高峰之间，不可能是小高峰和高峰之间

# 我思考题目思考的有问题！

def solution(arr):
    # dp(i)到节点i的左高峰
    max_value = -float('inf')
    left_dp = []
    for inx in range(len(arr)):
        left_dp.append(max_value)
        max_value = max(arr[inx], max_value)

    max_value = -float('inf')
    right_dp = []
    for inx in range(len(arr) - 1, -1, -1):
        right_dp.insert(0, max_value)
        max_value = max(arr[inx], max_value)

    # print(left_dp)
    # print(right_dp)
    ans = 0
    for inx in range(1, len(arr) - 1):
        con = min(left_dp[inx], right_dp[inx]) - arr[inx]
        if con > 0:
            ans += con
    return ans


if __name__ == '__main__':
    # n = 6
    # arr = [3, 1, 2, 5, 2, 4]
    # n = 5
    # arr = [4, 5, 1, 3, 2]

    n = int(input().strip())
    arr = list(map(int, input().strip().split()))
    ans = solution(arr)
    print(ans)