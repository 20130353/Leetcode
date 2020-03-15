# 就用max-min+1
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
    # 正常情况下在哪边都可以
    # 找某个元素的最大位置或者最小位置的停止条件必须是left=right，如果是left>right，不确定结果是left还是right
    # 找最小位置的时候出现的问题是mid一直在左边，可能出现死循环。
    # 应该是结果在那边mid在就落在那边
    while low < high:
        mid = low + (high + 1 - low) // 2
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
    print(ans_max - ans_min + 1)
