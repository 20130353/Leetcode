# 解决思路是：找到最长的回文子序列，然后用总长度-最长回文子序列
def getLongestPalindrome(a, n):
    dp = [[0] * n for _ in range(n)]
    for i in range(n - 1, -1, -1):
        dp[i][i] = 1
        if i + 1 < n and a[i] == a[i + 1]:
            dp[i][i + 1] = 2
        for j in range(i + 1, n):
            if a[i] == a[j]:
                if i + 1 < n and j - 1 >= 0:
                    dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                if i + 1 < n:
                    dp[i][j] = dp[i + 1][j]
                if j - 1 >= 0:
                    dp[i][j] = max(dp[i][j], dp[i][j - 1])

    # for i in range(n):
    #     print(dp[i])
    return n - max(max(dp))

if __name__ == '__main__':
    try:
        while True:
            string = input().strip()
            # string = 'google'
            ans = getLongestPalindrome(string, len(string))
            print(ans)
    except Exception as e:
        pass
