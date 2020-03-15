#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 解数独.py
# @Author: smx
# @Date  : 2020/2/19
# @Desc  :

# 暴力搜肯定超时！
class Solution:
    def DFS(self, board):
        print(board)
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    col = [board[c][j] for c in range(9)]
                    limit_i = i - i % 3
                    limit_j = j - j % 3
                    daj = []
                    for h in range(limit_i, i + 4 - limit_i):
                        for g in range(limit_j, j + 4 - limit_j):
                            daj.append(board[h][g])
                    for k in range(1,10):
                        if k not in board[i] and k not in col and k not in daj:
                            board[i][j] = str(k)
                            self.DFS(board)
                            board[i][j] = '.'

    def solveSudoku(self, board):
        if not board:
            return

        self.DFS(board)


if __name__ == '__main__':
    board = [['5', '3', '.', '.', '7', '.', '.', '.', '.'],
             ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
             ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
             ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
             ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
             ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
             ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
             ['.', '6', '.', '4', '1', '9', '.', '.', '5'],
             ['.', '.', '.', '.', '8', '.', '.', '7', '9']]
    Solution().solveSudoku(board)
    for each in board:
        print(board)
