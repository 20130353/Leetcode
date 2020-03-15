# -*- coding:utf-8 -*-
# 加入left最后一个和right最后一个的判断就过了！
# AC!
class Solution:
    def merge(self, left, right, count):
        if left[-1] <= right[0]:
            return left + right

        elif right[-1] <= left[0]:
            count[0] += left.__len__() * right.__len__()
            return right + left

        else:
            arr = []
            i, j = 0, 0
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    arr.append(left[i])
                    i += 1
                else:
                    count[0] += len(left) - i
                    arr.append(right[j])
                    j += 1
            if i != len(left):
                arr += left[i:]
            if j != len(right):
                arr += right[j:]
            return arr

    def merge_sort(self, arr, count):

        if len(arr) <= 1:
            return arr

        left = self.merge_sort(arr[:arr.__len__() // 2], count)
        right = self.merge_sort(arr[arr.__len__() // 2:], count)
        arr = self.merge(left, right, count)
        return arr

    def InversePairs(self, data):
        count = [0]
        _ = self.merge_sort(data, count)
        return count[0] % (1000000007)


if __name__ == '__main__':
    data = [1, 2, 3, 4, 5, 6, 7, 0]
    ans = Solution().InversePairs(data)
    print(ans)
