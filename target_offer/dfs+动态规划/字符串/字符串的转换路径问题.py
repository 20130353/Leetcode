#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 字符串的转换路径问题--字符串.py
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


def cmp(a, b):
    '''
    返回是否全部相等，不相等个数
    '''
    leng_cmp = abs(len(a) - len(b))

    if leng_cmp >= 2:
        return False, 2

    if leng_cmp == 0:
        if a == b:
            return True, 0
        nonum = 0
        for i in range(len(a)):
            if a[i] != b[i]:
                nonum += 1
        if nonum == 1:
            return False, 1
        return False, 2

    if leng_cmp == 1:
        if len(a) > len(b) and a[:-1] == b:
            return False, 1
        if len(a) < len(b) and b[:-1] == a:
            return False, 1
        return False, 2


def solution(arr, start, target, total_path, path):
    if start == target:
        if len(total_path) == 0 or len(path) == len(total_path[0]):
            total_path.append(path)
            return
        if len(path) < len(total_path[0]):
            total_path.clear()
            total_path.append(path)
            return

    for each in arr:
        if each not in path:
            is_cmp, nonum = cmp(start, each)
            next_path = path + ' -> ' + each
            if is_cmp or nonum == 1:
                solution(arr, each, target, total_path, next_path)


if __name__ == '__main__':
    n = int(input().strip())
    start, to = input().strip().split(' ')
    arr = []
    for _ in range(n):
        arr.append(input().strip())
    total_path = []
    solution(arr, start, to, total_path, ''.join(start))

    if len(total_path) >= 1:
        total_path = sorted(total_path)
        print('YES')
        for each in total_path:
            print(each)
    else:
        print('NO')
