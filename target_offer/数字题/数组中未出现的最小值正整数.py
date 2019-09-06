def solution(arr, n):
    # arr.sort()
    # for i in range(1, n):
    #     if arr[i] - arr[i - 1] != 1:
    #         return arr[i - 1] + 2 if arr[i - 1] + 1 <= 0 else arr[i - 1] + 1
    # return arr[n - 1] + 1

    for i in range(1, max(arr) + 2):
        if i not in arr:
            return i


if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    ans = solution(arr, n)
    print(ans)
