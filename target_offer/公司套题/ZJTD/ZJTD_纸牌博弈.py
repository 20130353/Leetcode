# 超时!
# 以后超时就用c++改写

if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    f = [[0] * n for _ in range(n)]
    s = [[0] * n for _ in range(n)]
    for j in range(n):
        f[j][j] = arr[j]
        s[j][j] = 0
        for i in range(j - 1, -1, -1):
            f[i][j] = max(arr[i] + s[i + 1][j], arr[j] + s[i][j - 1])
            s[i][j] = min(f[i + 1][j], f[i][j - 1])
    print(f[0][n - 1])


