# -*- coding: utf-8 -*-
# Author: sunmengxin
# time: 10/28/18
# file: 进阶版-线段树.py
# description:


'''
    上接之前的线段树

    区间更新是指更新多个叶子节点的值,如果一次更新完成需要多次更新重复节点,所以引入了延迟标记.
    延迟标记:记录这个节点是否发生更改,如果更改了需要修改其子节点的信息,并给子节点都标上相同的标记,同时消除掉当前节点的标记

    操作:
    1. 重新定义节点值,加上延迟标记
    2. 重新定义build建立树函数
    ...
    n. 重新构造所有相关函数

'''


class Node:
    def __init__(self, key):
        self.key = key
        self.mark = 0


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


def push_down(Tree, current_inx):
    if Tree[current_inx].mark != 0:
        # 因为左右孩子节点的标志可能被多次延迟,又没有向下传递
        Tree[current_inx * 2 + 1].mark += Tree[current_inx].mark
        Tree[current_inx * 2 + 2].mark += Tree[current_inx].mark

        # 因为求区间最小值,所以给区间的最小值也加上这个标记
        Tree[current_inx * 2 + 1].key += Tree[current_inx].mark
        Tree[current_inx * 2 + 2].key += Tree[current_inx].mark

        # 最后清空当前节点的标记
        Tree[current_inx].mark = 0


def query_segtree(Tree, current_inx, tree_start, tree_end, qu_start, qu_end):
    if qu_start < tree_start or qu_end > tree_end:
        return math.inf

    if qu_start >= tree_start and qu_end <= tree_end:
        return Tree[current_inx].key

    push_down(Tree, current_inx)  # 向下传递延迟标记

    # 区间最小值可能在左右两个子树中,所以取两个区间的最小值
    mid = int((tree_start + tree_end) / 2)
    left = query_segtree(Tree, current_inx * 2 + 1, tree_start, mid, qu_start, qu_end)
    right = query_segtree(Tree, current_inx * 2 + 2, mid, tree_end, qu_start, qu_end)

    return min(left, right)


def update(Tree, current_inx, up_start, up_end, tree_start, tree_end, data):
    if up_start < tree_start or up_end > tree_end:
        return math.inf
    if up_start >= tree_start and up_end <= tree_end:
        Tree[current_inx].key = data
        Tree[current_inx].mark += data
        return
    push_down(Tree, current_inx)
    mid = int((tree_start + tree_end) / 2)
    update(Tree, current_inx * 2 + 1, up_start, up_end, tree_start, mid, data)
    update(Tree, current_inx * 2 + 2, up_start, up_end, mid, tree_end, data)
    Tree[current_inx].key = min(Tree[current_inx * 2 + 1].key, Tree[current_inx * 2 + 2].key)


if __name__ == '__main__':
    data = [2, 5, 1, 4, 9, 3]
