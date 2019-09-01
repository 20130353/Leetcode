def solution(arr):
    dp = [0]
    max_value = -float('inf')
    for each in arr:
        dp.append(max(dp[-1] + each, each))
        max_value = max(max_value, dp[-1])
    return max_value


if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().strip().split()))
    ans = solution(arr)
    print(ans)
