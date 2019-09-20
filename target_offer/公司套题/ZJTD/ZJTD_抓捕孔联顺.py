# 内存超限:您的程序使用了超过限制的内存
# case通过率为20.00%

# 改成计算组合数
# 还是内存超过限制

# 不用mat数组，直接在计算dis时候就计算组合数的数量
# 运行超时:您的程序未能在规定时间内运行结束，请检查是否循环有错或算法复杂度过大。
# case通过率为20.00%

# 主要是发现有序，当最大的一个无法在d距离内达到，后面的也就都不用看了，所以就用指针指向最大的，然后收缩左指针
# 改成双指针
# 运行超时:您的程序未能在规定时间内运行结束，请检查是否循环有错或算法复杂度过大。
# case通过率为20.00%
# 双指针计算任选两个用(n-1)n/2的方式
# 这里有个技巧：固定首位避免重复！
# AC

# def solution(arr, n, mat, source_inx, cur_inx, path, total_path):
#     if path.__len__() == 3:
#         # print(path)
#         total_path[0] += 1
#         return
#
#     for i in range(cur_inx + 1, n):
#         if mat[source_inx][i] == 1 and arr[i] not in path:
#             solution(arr, n, mat, source_inx, i, path + [arr[i]], total_path)

# def solution(arr, n):
#     total_path = 0
#     for i in range(n):
#         count = 0
#         for j in range(i + 1, n):
#             if arr[j] - arr[i] <= d:
#                 count += 1
#             else:
#                 break
#         if count > 2:
#             fenzi = (reduce(lambda x, y: x * y, range(1, count + 1)))
#             fenmu = (reduce(lambda x, y: x * y, range(1, (count - 2) + 1))) * (
#                 reduce(lambda x, y: x * y, range(1, 2 + 1)))
#             total_path += fenzi / fenmu
#         elif count == 2:
#             total_path += 1
#     return total_path


def solution(arr, n):
    def C(n):
        return (n - 1) * n / 2

    if n <= 3:
        return 1

    i, j = 0, 2
    total_path = 0
    while i <= n - 3:
        while j < n and arr[j] - arr[i] <= d:
            j += 1
        count = j - 1 - i
        total_path += C(count)
        i += 1
    return total_path


if __name__ == '__main__':
    n, d = map(int, input().strip().split(' '))
    arr = list(map(int, input().strip().split(' ')))
    # n, d = 4, 3
    # arr = [1, 2, 3, 4]

    # n, d = 5, 19
    # arr = [1, 10, 20, 30, 50]

    arr.sort()
    ans = solution(arr, n)
    print('%d' % (ans % 99997867))
