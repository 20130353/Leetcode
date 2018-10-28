# -*- coding: utf-8 -*-
# Author: sunmengxin
# time: 10/27/18
# file: 线段树.py
# description:
'''

    线段树，类似区间树，它在各个节点保存一条线段（数组中的一段子数组），
    主要用于高效解决连续区间的动态查询问题，由于二叉结构的特性，
    基本能保持每个操作的复杂度为O(logn)。

    线段树的每个节点表示一个区间，子节点则分别表示父节点的左右半区间，
    例如父亲的区间是[a,b]，那么(c=(a+b)/2)左儿子的区间是[a,c]，
    儿子的区间是[c+1,b]。

'''


class Node:
    def __init__(self, key):
        self.key = key


import math


def build_segtree(Tree, current_indx, data, start, end):
    # 叶子节点
    if start == end:
        Tree[current_indx].key = data[start]
    else:
        # 区间节点
        mid = int((start + end) / 2)
        left_inx = current_indx * 2 + 1
        right_inx = current_indx * 2 + 2

        build_segtree(Tree, left_inx, data, start, mid)  # 构建左子树
        build_segtree(Tree, right_inx, data, mid + 1, end)  # 构建右子树

        # 设置父节点的值,父节点是左右子树中最小的值
        Tree[current_indx].key = min(Tree[left_inx].key, Tree[right_inx].key)


def query_segtree(Tree, current_inx, tree_start, tree_end, qu_start, qu_end):
    if qu_start < tree_start or qu_end > tree_end:
        return math.inf

    if qu_start >= tree_start and qu_end <= tree_end:
        return Tree[current_inx].key

    # 区间最小值可能在左右两个子树中,所以取两个区间的最小值
    mid = int((tree_start + tree_end) / 2)
    left = query_segtree(Tree, current_inx * 2 + 1, tree_start, mid, qu_start, qu_end)
    right = query_segtree(Tree, current_inx * 2 + 2, mid, tree_end, qu_start, qu_end)
    return min(left, right)


def update_one_ele(Tree, current_inx, start, end, index, key):
    if start == end:
        Tree[current_inx].key = key
        return

    mid = int((start + end) / 2)
    if index < mid:
        query_segtree(Tree, current_inx * 2 + 1, start, mid, index, key)
    else:
        query_segtree(Tree, current_inx * 2 + 2, mid, end, index, key)

    Tree[current_inx], key = min(Tree[current_inx * 2 + 1].key, Tree[current_inx * 2 + 2].key)  # 更新父节点的值


if __name__ == '__main__':
    data = [2, 5, 1, 4, 9, 3]
