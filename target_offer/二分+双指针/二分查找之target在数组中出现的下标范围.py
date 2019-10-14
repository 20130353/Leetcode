# 用low守住位置，不断更新low的位置，让high一直减小
def bineary_search_max(arr, n, target):
    '''
    找到最大位置
    '''
    low, high = 0, n - 1
    while low < high:
        mid = low + (high - low + 1) // 2
        if arr[mid] <= target:
            low = mid
        else:
            high = mid - 1
    return low if arr[low] == target else -1

def bineary_search_min(arr, n, target):
    '''
    找到最小位置
    '''
    low, high = 0, n - 1
    while low < high:
        mid = low + (high - low) // 2
        if arr[mid] >= target:  # 答案在包含这个位置的左边
            high = mid
        else:
            low = mid + 1
    return high if arr[high] == target else -1


if __name__ == '__main__':
    arr = [1, 2, 3, 3, 3, 4, 5, 7]
    # arr = [1]
    # arr = [1,1,1,1,1]
    ans_min = bineary_search_min(arr, len(arr), 3)
    ans_max = bineary_search_max(arr, len(arr), 3)
    print(ans_min, ans_max)
