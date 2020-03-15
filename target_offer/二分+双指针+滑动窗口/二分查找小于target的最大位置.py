# 找最大位置就用low守，找最小位置就用right守
def solution(arr, n, target):
    left, right = 0, n - 1
    # 如果使用low<=right,就不能加入mid元素，每次必须是mid加减1！
    while left < right:
        mid = left + (right - left + 1) // 2
        if arr[mid] < target:
            left = mid
        else:
            right = mid - 1
    if left >= n or arr[left] >= target:
        return -1
    return arr[left]


if __name__ == '__main__':
    arr = [1, 2, 3, 3, 3, 4, 5, 6, 7, 8]
    ans = solution(arr, len(arr), 4)
    print(ans)
