# 内存超限:您的程序使用了超过限制的内存
# case通过率为60.00%
# 解决方式：去掉main函数 --》 没用

# 内存超限:您的程序使用了超过限制的内存
# case通过率为60.00%

# 抽纸牌可以排序之后直接抽最大的，每次都是抽最大的，一定得到最大的差值
# AC

# def solution(arr,n):
#     arr.sort()
#     a, b = [[0] * n for _ in range(n)], [[0] * n for _ in range(n)]
#     for j in range(n):
#         a[j][j] = arr[j]
#         for i in range(j - 1, -1, -1):
#             a[i][j] = max(arr[i] + b[i + 1][j], arr[j] + b[i][j - 1])
#             b[i][j] = min(a[i + 1][j], a[i][j - 1])
#     total_score = sum(arr)
#     print(a[0][n - 1] - (total_score - a[0][n - 1]))
#

def solution(arr, n):
    arr.sort()
    arr.reverse()
    suma, sumb = 0, 0
    for i in range(n):
        if i & 1 == 0:
            suma += arr[i]
        else:
            sumb += arr[i]
    return suma - sumb


if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    ans = solution(arr, n)
    print(ans)
