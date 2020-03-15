# 找最大位置就用low守，找最小位置就用high守
def solution(arr, n, target):
    left, right = 0, n - 1
    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] > target:
            right = mid
        else:
            left = mid + 1
    if right < 0 or arr[right] <= target:
        return -1
    return right, arr[right]


if __name__ == '__main__':
    arr = [1, 2, 3, 3, 3, 4, 5, 6, 7, 8]
    ans = solution(arr, len(arr), 9)
    print(ans)
