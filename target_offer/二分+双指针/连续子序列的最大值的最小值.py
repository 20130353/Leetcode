# 输入一个序列判断所有长度为k的连续子序列中的最大值中的最小值。
# 每个连续子序列中都有一个最大值，所有最大值的最小值。
# 解题思路：滑动窗口找到长度为k的子序列，保存最大值就找到最小值了。

def solution(arr, k):
    i, j = 0, k

    min_value = float('inf')
    while j <= len(arr):
        min_value = min(min_value, max(arr[i:j]))
        i += 1
        j += 1
    return min_value


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6]
    k = 2
    ans = solution(arr, k)
    print(ans)
