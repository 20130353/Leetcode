# -*- coding: utf-8 -*-
# author: sunmengxin
# time: 18-11-25
# file: 扑克牌顺子
# description:

# 反思:写代码写的太快了,没有及时检查给定的数组是否为空的问题
class Solution:
    def IsContinuous(self, numbers):

        if not numbers:
            return False

        sorted_arr = sorted(numbers)
        count = 0
        pre = None
        for each in sorted_arr:
            if each == 0:
                count += 1
            elif pre == None:
                pre = each
            else:
                if each == pre:
                    return False
                elif each - pre == 1:
                    pre = each
                else:
                    count -= each - pre - 1
                    if count < 0:
                        return False
                    pre = each
        return True

if __name__ == '__main__':
    so = Solution()
    print(so.IsContinuous([0,3,2,6,4]))