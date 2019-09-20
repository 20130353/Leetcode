# 关键点是对已经排好的情侣，不计算交换次数
# 我自己的想法是太关注左右移动带来的count计数不同的问题
def solution(arr, n):
    mark = [1] * n
    i = 0
    count = 0
    while i < n:
        if mark[i] == 1:
            j = i + 1
            while j < n and arr[j] != arr[i]:
                count += mark[j]
                j += 1
            mark[j] = 0
            mark[i] = 0
        i += 1
    return count


if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    ans = solution(arr, n * 2)
    print(ans)
