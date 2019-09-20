# 存在的问题：只能找到三个点，但是存在多个最大点的情况
# def solution(arr):
#     ans = []
#     arr.sort(key=lambda x: x[0])
#     ans.append(arr[-1])
#
#     arr.sort(key=lambda x: x[1])
#     if arr[-1] not in ans:
#         ans.append(arr[-1])
#
#     max_p = (-1, -1)
#     for each in arr:
#         if each[0] + each[1] > max_p[0] + max_p[1]:
#             max_p = each
#     if max_p not in ans and ans[0][1] <= max_p[1] and ans[1][0] <= max_p[0]:
#         ans.append(max_p)
#
#     ans.sort(key=lambda x: x[0])
#     return ans

# 运行超时:您的程序未能在规定时间内运行结束，请检查是否循环有错或算法复杂度过大。
# case通过率为80.00%

# 去掉最后的排序
# 还是超时！
# 用C++AC


def solution(arr):
    ans = []
    arr.sort(key=lambda x: x[0])
    ans.append(arr[-1])

    pre_y = ans[0][1]
    for i in range(n - 2, -1, -1):
        if arr[i][1] >= pre_y:
            ans.append(arr[i])
            pre_y = ans[-1][1]

    # ans.sort(key=lambda x: x[0])
    return ans[::-1]


if __name__ == '__main__':
    n = int(input().strip())
    arr = []
    for _ in range(n):
        a, b = map(int, input().strip().split(' '))
        arr.append((a, b))
    ans = solution(arr)
    for each in ans:
        print('%d %d' % (each[0], each[1]))
