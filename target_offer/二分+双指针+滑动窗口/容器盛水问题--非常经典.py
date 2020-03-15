
# 思路：固定某个点，最大面积就是以当前点作为最小的最远面积，遍历所有点即可。
# 因为双向，所有可以用两个指针，来回指定
class Solution:
    def maxArea(self, arr):
        if not arr or len(arr) <= 1:
            return 0

        left, right = 0, len(arr) - 1
        max_value = -0xffffff
        while left != right:
            max_value = max((right - left) * min(arr[left], arr[right]), max_value)
            if arr[left] <= arr[right]:
                left += 1
            else:
                right -= 1
        return max_value


if __name__ == '__main__':
    arr = [1, 3, 5, 4, 2, 6, 8, 3, 2]
    ans = Solution().maxArea(arr)
    print(ans)
