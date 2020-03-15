def solution(n):
    dp = [0, 1, 2] + [0] * (n - 1)
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]


if __name__ == '__main__':
    try:
        while True:
            string = input().strip()
            if string == '':
                break
            n = int(string)
            ans = solution(n)
            print(ans)
    except Exception as e:
        print('run error!')
        print(e)