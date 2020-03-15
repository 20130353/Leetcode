#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 火眼金睛.py
# @Author: smx
# @Date  : 2019/8/27
# @Desc  :


# 现在我们需要查出一些作弊的问答社区中的ID，作弊有两种：1.A回答了B的问题，同时B回答了A的问题。
# 那么A和B都是作弊。2.作弊ID用户A和作弊ID用户B同时回答了C的问题，那么C也是作弊。已知每个用户的ID是一串数字，一个问题可能有多个人回答。
# 开始想用集合保存被回答的集合和回答的集合，但是后来觉得空间没有必要，用矩阵更好，所以直接优化成矩阵


# 存在的问题：自己回答自己的问题不算作弊！
# 存在的问题：您的代码已保存
# 答案错误:您提交的程序没有通过所有的测试用例
# case通过率为0.00%
# 没有多组输入

# 存在的问题：您的代码已保存
# 答案错误:您提交的程序没有通过所有的测试用例
# case通过率为20.00%
# 没有去重

# 存在的问题：您的代码已保存
# 答案错误:您提交的程序没有通过所有的测试用例
# case通过率为40.00%
# 没有排序
# AC



try:
    while True:
        n = int(input().strip())
        mat = [[0] * (n + 1) for _ in range(n + 1)]
        ans = []
        for _ in range(n):
            arr = list(map(int, input().strip().split(' ')))
            cur, num = arr[0], arr[1]
            count = 0
            for i in range(2, 2 + num):
                mat[arr[i]][cur] = 1
                if cur != arr[i] and mat[cur][arr[i]] == 1:
                    count += 1
                    if arr[i] not in ans:
                        ans.append(arr[i])
                    if cur not in ans:
                        ans.append(cur)
            if cur not in ans and len(set(ans) & set(arr[2:])) >= 2:
                ans.append(cur)
        print(len(ans))
        if len(ans) > 0:
            print(' '.join(list(map(str, sorted(ans)))))
except:
    pass
