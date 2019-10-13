#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 迷雾.py
# @Author: smx
# @Date  : 2019/8/27
# @Desc  :

# 随便输入输出就然可以过90%。。。
# 答案错误:您提交的程序没有通过所有的测试用例
# case通过率为90.00%
#
# 用例:
# 10
# 71468952310
#
# 对应输出应该为:
#
# 7 1 4 6 8 9 5 2 3 10
#
# 你的输出为:
#
# 7 1 4 6 8 9 5 2 3 1 0

# 题目原来想表达的意思如下：
# 例如给定n=25，那么现在总共有25个数字，从1到25，正常的顺序把它们连起来写是这样：12345678910111213141516171819202122232425，
# 而现在把这些顺序进行了打乱，问你原来可能是什么样子的组合。
# 可以用字符串分割的方式，根据给定的最大值判断是否可分割 + 是否当前这个数字被分割过 +  分割结果正好是原来的数字个数
# 测试用例不严谨，没有保证每个数字只出现一次也可以全部AC！
# 后面加上set保证每个数字只出现一次 + 不能有0！
# 和字符串的解码是一样的题目！
def solution(string, n, cur, ans):
    if string == '':
        if len(set(cur)) == n:
            ans.append(' '.join(cur) + ' ')
        return

    count = 1
    while count <= string.__len__() and int(string[:count]) <= n and int(string[:count]) >= 1:
        solution(string[count:], n, cur + [string[:count]], ans)
        count += 1


if __name__ == '__main__':
    try:
        while True:
            first = input().strip()
            if first == '':
                break
            n = int(first)
            string = input().strip()
            ans = []
            solution(string, n, [], ans)
            for each in ans:
                print(each)
    except Exception:
        pass
