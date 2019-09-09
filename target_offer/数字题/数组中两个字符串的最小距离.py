# 存在的问题：
# 没有考虑重复元素的位置最近
# 如果用max-min不一定能得到最近的距离
# 这样也不能得到最近距离
# min_A, max_A = min(A), max(A)
# min_B, max_B = min(B), max(B)
# return min(abs(min_A - min_B), abs(max_A - max_B), abs(min_A - max_B), abs(max_A - min_B))

# 如果用先找出来在遍历的方式，浪费时间，可以在遍历的时候就记录下最小的距离
# def solution(arr, n, source, target):
#     if source not in arr or target not in arr:
#         return -1
#
#     if source == target:
#         return 0
#
#     A, B = [], []
#     for k in range(n):
#         if arr[k] == source:
#             A.append(k)
#         if arr[k] == target:
#             B.append(k)
#
#     min_dis = float('inf')
#     for i in A:
#         for j in B:
#             min_dis = min(abs(i - j), min_dis)
#     return min_dis
#     # min_A, max_A = min(A), max(A)
#     # min_B, max_B = min(B), max(B)
#     # return min(abs(min_A - min_B), abs(max_A - max_B), abs(min_A - max_B), abs(max_A - min_B))


# 保留位置
def solution(arr, n, source, target):
    if source not in arr or target not in arr:
        return -1

    if source == target:
        return 0

    min_dis = float('inf')
    last_i, last_j = -1, -1
    for k in range(n):
        if arr[k] == source:
            last_i = k
            min_dis = min(min_dis, abs(last_i - last_j)) if last_j != -1 else min_dis
        if arr[k] == target:
            last_j = k
            min_dis = min(min_dis, abs(last_i - last_j)) if last_i != -1 else min_dis
    return min_dis


if __name__ == '__main__':

    n = int(input().strip())
    source, target = input().strip().split(' ')
    arr = []
    for _ in range(n):
        arr.append(input().strip())

    ans = solution(arr, n, source, target)
    print(ans)
