from collections import Counter


def solution(arr, n):
    if n == 0:
        return 0
    if n == 1:
        return arr
    if n == 2:
        return abs(arr[0] - arr[1])

    counter = Counter(arr)
    sorted_arr = list(counter.elements())

    total_sum = sum(arr)
    max_gap = -float('inf')
    pre_sum = 0
    for i in range(n - 1):
        pre_sum += sorted_arr[i]
        A_avg = pre_sum / i if i != 0 else pre_sum
        B_avg = (total_sum - pre_sum) / (n - i - 1)
        if abs(A_avg - B_avg) > max_gap:
            max_gap = abs(A_avg - B_avg)
    return max_gap


if __name__ == '__main__':
    arr = [0, 1, 2, 5, 3, 9, 5, 7, 8]
    ans = solution(arr, len(arr))
    print(ans)
