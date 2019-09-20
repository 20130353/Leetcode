# 请检查是否存在语法错误或者数组越界非法访问等情况
# case通过率为0.00%
# 不是这个问题！是因为输入有问题!

# 内存超限:您的程序使用了超过限制的内存
# case通过率为10.00%
# 思路没错，但是可以找到规律
# def solution(n, m):
#     mat = [[0] * m for _ in range(n)]  # 0表示正面
#     dir = [[0, 1], [0, -1], [-1, 0], [1, 0], [-1, -1], [1, 1], [-1, 1], [1, -1]]
#     for i in range(n):
#         for j in range(m):
#             mat[i][j] = 1 if mat[i][j] == 0 else 0
#             for k in range(8):
#                 if i + dir[k][0] >= 0 and i + dir[k][0] < n and j + dir[k][1] >= 0 and j + dir[k][1] < m:
#                     mat[i + dir[k][0]][j + dir[k][1]] = 1 if mat[i + dir[k][0]][j + dir[k][1]] == 0 else 0
#     ans = 0
#     for i in range(n):
#         ans += sum(mat[i])
#     return ans


# 分为四种情况
# 答案错误:您提交的程序没有通过所有的测试用例
# case通过率为90.00%

# 存在的问题：大数的乘积超过限制！
# 这种可以通过换成c++实现

def solution(n, m):
    if n == 1 and m == 1:
        return 1
    if n == 1 and m > 1:
        return m - 2
    if n > 1 and m == 1:
        return n - 2
    return (n - 2) * (m - 2)


if __name__ == '__main__':

    n = int(input().strip())
    for i in range(n):
        n, m = map(int, input().strip().split(' '))
        print(solution(n, m))
