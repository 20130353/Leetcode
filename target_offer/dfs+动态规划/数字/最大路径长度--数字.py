#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 最大路径长度--数字.py
# @Author: smx
# @Date  : 2019/8/12
# @Desc  :

# 给定一颗二叉树和一个整数 sum，求累加和为 sum 的最长路径长度。路径是指从某个节点往下，每次最多选择一个孩子节点或者不选所形成的节点链。
#  总结这道题：
# 1. 审题， 没有理解不选这个节点的意思是不选这个节点及其子节点
# 2. 即使已经算出来了target，但是不能结束，需要一直走到根节点才行,所以必须用map保存走过的路径和，判断是否存在sum-target存在的情况。
# 这里不用能走不走因为不走这个节点就会错过这个节点下面的路径可能和为target的情况
# 3. 用全局的可变变量和不可变变量，不可变变量的写法更清楚，时间和内存的消耗都比较少！
# 4. 用邻接表的方式（map），不用树结构的方法应该可以更省内存！

class Node:
    def __init__(self):
        self.left = None
        self.right = None
        self.val = float('inf')

def solution(T, target, cur_sum, leng, max_value, dict):
    if not T:
        return max_value
    cur_sum = cur_sum + int(T.val)
    if cur_sum not in dict:
        dict[cur_sum] = leng
    if cur_sum - target in dict:
        max_value = max(max_value, leng - dict[cur_sum - target])
    max_value = solution(T.left, target, cur_sum, leng + 1, max_value, dict)
    max_value = solution(T.right, target, cur_sum, leng + 1, max_value, dict)
    if leng == dict.get(cur_sum):
        dict.pop(cur_sum)
    return max_value


#
# def solution(T, target, cur_sum, leng, max_value, dict):
#     if not T:
#         return max_value
#     cur_sum += T.val
#     if cur_sum not in dict:
#         dict[cur_sum] = leng
#     if cur_sum - target in dict:
#         max_value[0] = max(max_value[0], leng - dict[cur_sum - target])
#
#     solution(T.left, target, cur_sum, leng + 1, max_value, dict)
#     solution(T.right, target, cur_sum, leng + 1, max_value, dict)
#
#     if leng == dict.get(cur_sum):
#         dict.pop(cur_sum)


if __name__ == '__main__':
    n, root = map(int, input().strip().split())
    yueshu_dict = {root: Node()}

    for i in range(n):
        fa, left, right, val = map(int, input().strip().split())
        if yueshu_dict.get(fa) is None:
            yueshu_dict[fa] = Node()
        if left != 0 and yueshu_dict.get(left) is None:
            yueshu_dict[left] = Node()
            yueshu_dict[fa].left = yueshu_dict[left]
        if right != 0 and yueshu_dict.get(right) is None:
            yueshu_dict[right] = Node()
            yueshu_dict[fa].right = yueshu_dict[right]
        yueshu_dict[fa].val = val

    target = int(input().strip())
    ans = [0]
    solution(yueshu_dict[root], target, 0, 1, ans, {0: 0})
    print(ans[0])
