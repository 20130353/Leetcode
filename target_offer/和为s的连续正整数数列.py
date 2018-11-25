# -*- coding: utf-8 -*-
# author: sunmengxin
# time: 18-11-25
# file: 和为s的连续正整数数列
# description:


# 反思：
# 1. while循环的变量的变化标注一定不要错！
# 2. 这个题目的解法可以参考回文子串的解法,用中心扩展的原理,但是时间复杂度没有减少


# class Solution:
#     def FindContinuousSequence(self, tsum):
#         # write code here
#         if tsum <= 0:
#             return 0
#
#         output = []
#         for i in range(1, (tsum + 1) // 2):
#             left, right = i, (tsum + 1) // 2
#             while left <= right:
#                 sn = (left + right) * (right - left + 1) / 2
#                 if sn == tsum:
#                     output.append([i for i in range(left, right + 1)])
#                     break
#                 elif sn < tsum:
#                     left += 1
#                 else:
#                     right -= 1
#         return output


# 用中心扩展的方式解决问题
class Solution:

    def sequence_sum(self, left, right, min_value, max_value, tsum, output):

        while left >= min_value and right <= max_value:
            sn = (left + right) * (right - left + 1) / 2
            if sn == tsum:
                output.append([i for i in range(left, right + 1)])
                return
            elif sn < tsum:
                left -= 1
                right += 1
            else:
                break
        return

    def FindContinuousSequence(self, tsum):
        # write code here
        if tsum <= 0:
            return 0

        output = []
        min_value = 1
        max_value = (tsum + 1) // 2
        for i in range(1, (tsum + 1) // 2):
            # 第一种作为奇数的尝试
            self.sequence_sum(i - 1, i + 1, min_value, max_value, tsum, output)

            # 第二种作为偶数的尝试
            self.sequence_sum(i, i + 1, min_value, max_value, tsum, output)
            # print(output)
        return output


if __name__ == '__main__':
    so = Solution()
    # print(so.FindContinuousSequence(10))
    print(so.FindContinuousSequence(15))
