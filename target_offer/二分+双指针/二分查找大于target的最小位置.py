# 找最大位置就用low守，找最小位置就用high守
def solution(arr, n, target):
    low, high = 0, n - 1
    while low < high:
        mid = low + (high - low) // 2
        if arr[mid] > target:
            high = mid
        else:
            low = mid + 1
    return arr[high]

if __name__ == '__main__':
    arr = [1, 2, 3, 3, 3, 4, 5, 6, 7, 8]
    ans = solution(arr, len(arr), 3)
    print(ans)
