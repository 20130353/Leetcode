#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 击败魔物.py
# @Author: smx
# @Date  : 2019/8/18
# @Desc  :
#
# 今天做笔试存在的问题：
# 1. 01背包超时！ -》 自己单独熟练01背包问题，不能动态规划的那种
# 2. 最后一个问题的答案想的有点简单了，到后面没有时间了
#
# 今天做的比较好的点是：背包通过测试多个case，提高了AC成绩！以后再接再厉！


# # 存在的问题： 直接计算出来的答案不一定是最优解,每次应该多计算几组解
# 存在的问题：确定x的上界和下界，上界为血量最高的怪物，下界为T回合输出刚好为怪物血量的总和，然后贪心测试是否合法，二分查找x
# 存在的问题：最后结束二分查找的时候不一定是正确解，需要判断一下。

# 为什么当时没有做出来？ 当时没有考虑到找技能的方式，只想到暴力，但是找不到上界
# 下次遇到找解的时候，一定要确定上下界，然后二分查找

# def solution(n, t, m, asum):
#     if m == 0:
#         if asum > t:
#             return -1
#         else:
#             return 0
#     x = (asum - (t - m)) * 1.0 / m
#     x_int = int(x)
#     if x_int != x:
#         ans = x_int + 1
#         if ans == 1:
#             return 0
#         else:
#             return ans
#     else:
#         if x_int == 1:
#             return 0
#         else:
#             return x_int
import copy as cp


def judge(key, t, m, arr):
    narr = cp.deepcopy(arr)
    ans = False

    while len(narr) > 0:
        narr.sort()
        max_value = narr.pop(-1)

        need_cost = max_value / key
        if int(need_cost) != need_cost:
            need_cost = int(need_cost) + 1
        cost = min(need_cost, m)

        t -= cost
        m -= cost
        if max_value - cost * key > 0:
            narr.append(max_value - cost * key)

        if m <= 0:
            if sum(narr) <= t:
                ans = True
            return ans

        if t <= 0:
            if len(narr) <= 0:
                ans = True
            return ans
    return True


# 技能的上界是血量最大值，因为每次打一个怪物即使多余很多伤害，也必须使用一次！
# 如果是所有怪物的总和，也是没有必要的。因为会不断下降到血量最大值
def solution(t, m, arr):
    low, high = 0, max(arr)
    while low < high:
        mid = low + (high - low) // 2
        flag = judge(mid, t, m, arr)
        if flag:
            high = mid
        else:
            low = mid + 1

    flag = judge(low, t, m, arr)
    if flag:
        return low
    else:
        return -1


if __name__ == '__main__':
    n, t, m = map(int, input().strip().split(' '))
    arr = list(map(int, input().strip().split(' ')))
    ans = solution(t, m, arr)
    print(ans)
