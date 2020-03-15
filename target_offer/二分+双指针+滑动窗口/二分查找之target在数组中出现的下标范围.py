# 二分查找的时间复杂度：
# 分析：每次遍历区间是n/2，n/4，1，中间的操作时间是O(1)，所以整体时间循环次数*单次时间=O(logn)
# 和快速排序的区别是，中间的操作时间是O(n)，所以是O(nlogn)
# 最好时间是O(1)，最坏时间是O(logn)

def binary_search(arr, n, target):
    if not arr:
        return -1
    left, right = 0, n - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1


# 用low守住位置，不断更新low的位置，让high一直减小
def binary_search_max(arr, n, target):
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


def binary_search_min(arr, n, target):
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
    ans = binary_search(arr, len(arr), 3)
    ans_min = binary_search_min(arr, len(arr), 3)
    ans_max = binary_search_max(arr, len(arr), 3)
    print(ans, ans_min, ans_max)
