# def solution(arr):
#     ans = 0
#     for i in range(1, arr.__len__()):
#         ans += arr[i - 1] - arr[i]
#     # print(ans)
#     return (-ans) + arr[0] if ans <= 0 else arr[0]


# 没有找到数字之间的规律!
# AC
# def solution(arr):
#     for i in range(max(arr) + 1):
#         E = i
#         for j in range(1, arr.__len__()):
#             print('E {},arr[j] {}'.format(E, arr[j]))
#             if arr[j] >= E:
#                 E -= (arr[j] - E)
#             else:
#                 E += (E - arr[j])
#             if E < 0:
#                 break
#         if E >= 0 and j == arr.__len__() - 1:
#             return i
#     return -1


def solution(arr, n):
    E = 0
    for i in range(n - 1, -1, -1):
        E = (E + arr[i] + 1) >> 1
    return E


if __name__ == '__main__':
    # n = 5
    # arr = [3, 4, 3, 2, 4]
    # n = 3
    # arr = [4, 4, 4]
    # n = 3
    # arr = [1, 6, 4]
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    ans = solution(arr, n)
    print(ans)
