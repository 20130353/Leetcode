# 用low守住位置，不断更新low的位置，让high一直减小
def bineary_search_max(arr, n, target):
    '''
    找到最大位置
    :param arr:
    :param n:
    :param target:
    :return:
    '''
    low, high = 0, n - 1
    while low < high:
        if low + 1 == high:
            mid = low + (high + 1 - low) // 2
        else:
            mid = low + (high - low) // 2
        if arr[mid] <= target:  # 答案在包含这个位置的右边
            low = mid
        else:
            high = mid - 1
    return low if arr[low] == target else -1


# 用high守住位置，不断更新high的位置，让low一直增大
def bineary_search_min(arr, n, target):
    '''
    找到最大位置
    :param arr:
    :param n:
    :param target:
    :return:
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
    print(ans_min)
    print(ans_max)
