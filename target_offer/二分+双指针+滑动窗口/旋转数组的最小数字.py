# -*- coding: utf-8 -*-
# Author: sunmengxin
# time: 10/10/18
# file: 旋转数组的最小数字.py
# description:


'''
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。
例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。
'''


class Solution:
    def minNumberInRotateArray(self, rotateArray):
        if len(rotateArray) == 0 or rotateArray == None:
            return 0

        left, right = 0, len(rotateArray) - 1
        min_value = rotateArray[left]
        while right - left > 1:
            mid = int((left + right) / 2)
            if rotateArray[mid] > rotateArray[left]:
                left = mid
            elif rotateArray[mid] < rotateArray[right]:
                right = mid
            # 如果出现等于了-->不能确定是哪一边
            elif rotateArray[mid] == rotateArray[left] and rotateArray[mid] == rotateArray[right]:
                for i in range(left, right):
                    min_value = min(rotateArray[i], min_value)

        min_value = rotateArray[right]
        return min_value


if __name__ == '__main__':
    so = Solution()

    print(so.minNumberInRotateArray([3, 4, 5, 1, 2]))
    # print(minvalue([1, 2, 3, 4, 5]))
    # print(minvalue([1, 1, 1, 0, 1]))
    # print(minvalue([1, 0, 1, 1, 1]))
    # print(minvalue([]))
    # print(minvalue([1]))
