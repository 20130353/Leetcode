#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 字符串的转换路径问题--字符串--区间动规.py
# @Author: smx
# @Date  : 2019/8/13
# @Desc  :

# 存在的问题：改变一个字符是否包括删除或者增加一个字符的情况呢？
# 存在的问题：没有通过所有的测试样例 --> 我理解错了，我不应该用剩下的字符去匹配，应该直接是转换后得到的新字符去变成target字符
# 存在的问题：一直是语法错误或者数组越界非法访问等情况！ --> 运行内存太大了
# 这个可以转换为dp，但是需要回溯才能找到路径，不如递归省事

# def solution(arr, start, target, flag, total_path, path):
#     if ''.join(target) not in arr:
#         return
#
#     if start == target or (len(start) == 0 and len(target) == 0):
#         flag[0] = True
#         total_path.append(path)
#         return
#
#     if len(start) <= 0 or len(target) <= 0:
#         return
#
#     print('start,target', start, target)
#     if start[0] == target[0]:
#         print('==')
#         solution(arr, start[1:], target[1:], flag, total_path, path + ' -> ' + ''.join(start))
#
#     temp = start[0]
#     start[0] = target[0]
#     # 第一种情况：变换
#     if ''.join(start) in arr:
#         print('delete')
#         solution(arr, start[1:], target[1:], flag, total_path, path + ' -> ' + ''.join(start))
#
#     # 第二种情况：删除
#     temp = start[1:]
#     if ''.join(temp) in arr:
#         print('add')
#         solution(arr, temp, target, flag, total_path, path + ' -> ' + ''.join(temp))
#
#     # 第三种情况：增加
#     temp = list(target[0]) + start
#     if ''.join(temp) in arr:
#         solution(arr, temp, target, flag, total_path, path + ' -> ' + ''.join(temp))


# 这个比较可以用双指针完成，一个指针指向A，一个指针指向B，
# 检查两个指针对应的字符是否相等，如果相等跳过，如果不相等就增加删除改变一个字符，限制只能一次，如果多次之后不能就不能。
# 核心思想就是跳过这个字符！
# 请检查是否存在语法错误或者数组越界非法访问等情况 --> 测试用例不通过！

# 运行超时:您的程序未能在规定时间内运行结束，请检查是否循环有错或算法复杂度过大。
# case通过率为0.00%

# 改进方法：提前准备好cmp的结果，同时把可以走通的路径标好，一旦走到可以走到的路径就直接加入！
# 还是复杂度过大！
import copy as cp


def solution(arr, start, target, total_path, path, dict):
    if start == target:
        if len(total_path) == 0 or len(path) == len(total_path[0]):
            total_path.append(path)
            return
        if len(path) < len(total_path[0]):
            total_path.clear()
            total_path.append(path)
            return

    for each in dict[start]:
        # print('start {},dict[start] {}'.format(start, dict[start]))
        if each not in path:
            next_path = cp.deepcopy(path)
            next_path.append(each)
            solution(arr, each, target, total_path, next_path, dict)


def find_neighboring_vertex(arr, n):
    def cmp(a, b):
        if abs(a.__len__() - b.__len__()) >= 2:
            return False

        i, j, k = 0, 0, 0
        while i < a.__len__() and j < b.__len__():
            if a[i] == b[j]:
                i += 1
                j += 1
            else:
                if k == 0:
                    k = 1
                else:
                    return False
                if a.__len__() == b.__len__():
                    i += 1
                    j += 1
                elif a.__len__() < b.__len__():
                    j += 1
                else:
                    i += 1
        return True

    dict = {}
    for i in range(n):
        for j in range(i + 1, n):
            # print('arr[i] {},arr[j] {}'.format(arr[i], arr[j]))
            if cmp(arr[i], arr[j]):
                if arr[i] not in dict.keys():
                    dict[arr[i]] = [arr[j]]
                else:
                    dict[arr[i]].append(arr[j])

                if arr[j] not in dict.keys():
                    dict[arr[j]] = [arr[i]]
                else:
                    dict[arr[j]].append(arr[i])
    return dict


if __name__ == '__main__':
    try:
        n = int(input().strip())
        start, to = input().strip().split(' ')
        arr = [start]
        for _ in range(n):
            arr.append(input().strip())

        dict = find_neighboring_vertex(arr, n + 1)
        total_path = []
        solution(arr, start, to, total_path, [start], dict)

        if len(total_path) >= 1:
            total_path = sorted(total_path)
            print('YES')
            for each_path in total_path:
                ans = each_path[0]
                for i in range(1, len(each_path)):
                    ans += ' -> ' + each_path[i]
                print(ans)
        else:
            print('NO')
    except Exception as e:
        print(e)
