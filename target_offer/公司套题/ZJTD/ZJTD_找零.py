# AC
def solution(n):
    dp = [0] + [float('inf')] * n
    arr = [1, 4, 16, 64]
    for i in range(1, n + 1):
        for j in range(arr.__len__()):
            if i >= arr[j]:
                dp[i] = min(dp[i], dp[i - arr[j]] + 1)
    # print(dp)
    return dp[n]


if __name__ == '__main__':
    n = int(input().strip())
    ans = solution(1024 - n)
    print(ans)
