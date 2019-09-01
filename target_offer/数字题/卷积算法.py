#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 卷积算法.py
# @Author: smx
# @Date  : 2019/8/20
# @Desc  :


if __name__ == '__main__':
    h, w = map(int, input().strip().split(' '))
    mat = []
    for _ in range(h):
        mat.append(list(map(int, input().strip().split(' '))))
    m = int(input().strip())
    m_ker = []
    for _ in range(m):
        m_ker.append(list(map(float, input().strip().split(' '))))

    ans = [[0] * (w - m + 1) for _ in range(h - m + 1)]
    for i in range(h - m + 1):
        for j in range(w - m + 1):
            temp_ans = 0
            for x in range(m):
                for y in range(m):
                    temp_ans += mat[i + x][j + y] * m_ker[x][y]
            ans[i][j] = int(min(temp_ans, 255))
    for i in range(h - m + 1):
        print(' '.join(map(str, ans[i])))
