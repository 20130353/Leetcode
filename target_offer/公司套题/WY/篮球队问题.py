# 暴力递归
# 运行超时:您的程序未能在规定时间内运行结束，请检查是否循环有错或算法复杂度过大。
# case通过率为30.00%


# 增加剪枝条件
# 运行超时:您的程序未能在规定时间内运行结束，请检查是否循环有错或算法复杂度过大。
# case通过率为30.00%
# def judge(sum1, sum2, s1):
#     if sum1 <= sum2 or sum1 - sum2 >= 2 * min(s1):
#         return False
#     return True
#
# def solution(n, cur_pos, arr, s1, s2, ns1, ns2, count):
#     if n == 1:
#         count[0] = 1
#         return
#
#     if cur_pos == n:
#         if judge(ns1, ns2, s1):
#             count[0] += 1
#         return
#
#     if ns1 + sum(arr[cur_pos:]) <= ns2:
#         return
#
#     s1.append(arr[cur_pos])
#     solution(n, cur_pos + 1, arr, s1, s2, ns1 + arr[cur_pos], ns2, count)
#     s1.pop()
#
#     s2.append(arr[cur_pos])
#     solution(n, cur_pos + 1, arr, s1, s2, ns1, ns2 + arr[cur_pos], count)
#     s2.pop()

# 只能过30% -- 所以一定有动归方程
# 之前以为是Asum和Bsum的之间影响，没有子问题，所以就没想动态规划！
# 但是Bsum可以写成总sum-Asum，就转换成了一个问题。

# 运行超时:您的程序未能在规定时间内运行结束，请检查是否循环有错或算法复杂度过大。
# case通过率为40.00%
def solution(arr, n):
    arr.sort(reverse=True)
    tsum = sum(arr)
    dp = [1] + [0] * tsum
    ans = 0
    for i in range(n):
        for j in range(tsum, arr[i] - 1, -1):
            dp[j] += dp[j - arr[i]]
            # 为什么这里只计算放入A的情况，不计算不放入A队的情况呢？
            if j > tsum - j and j - arr[i] < tsum - j + arr[i]:
                ans += dp[j - arr[i]]
    return ans


if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    ans = solution(arr, n)
    print(ans)
