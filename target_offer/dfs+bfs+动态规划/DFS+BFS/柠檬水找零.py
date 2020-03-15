#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 柠檬水找零.py
# @Author: smx
# @Date  : 2020/2/21
# @Desc  :


# 这道题用贪心的思想，每次用少的5元去找零钱！
class Solution:
    def lemonadeChange(self, arrs):
        if not arrs: return True
        num_dict = {5: 0, 10: 0, 20: 0}
        for i in range(len(arrs)):
            change = arrs[i] - 5
            if change == 0:
                num_dict[arrs[i]] += 1
            elif change == 5:
                if num_dict[change] <= 0:
                    return False
                else:
                    num_dict[change] -= 1
                    num_dict[arrs[i]] += 1
            elif change == 15:
                if num_dict[5] >= 1 and num_dict[10] >= 1:
                    num_dict[5] -= 1
                    num_dict[10] -= 1
                    num_dict[arrs[i]] += 1
                elif num_dict[5] >= 3:
                    num_dict[5] -= 3
                    num_dict[arrs[i]] += 1
                else:
                    return False
        return True


if __name__ == '__main__':
    arrs = [5,5,5,10,20]

    print(Solution().lemonadeChange(arrs))
