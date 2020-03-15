#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 单词接龙2.py
# @Author: smx
# @Date  : 2020/2/21
# @Desc  :
class Solution:
    def findLadders(self, start_word: str, end_word: str, words: list) -> list:
        words = set(words)  # 转换为hash实现O(1)的in判断

        if end_word not in words:
            return []

        res = []
        visited = set()
        forward = {start_word: [[start_word]]}
        backward = {end_word: [[end_word]]}
        _len = 2

        while forward:
            if len(forward) > len(backward):  #双向BFS每次从较少的队列开始扩展
                forward, backward = backward, forward
            tmp = {}  # 存储新的前向分支
            while forward:
                word, paths = forward.popitem()  # 取出路径结束词以及到达它的所有路径
                visited.add(word)  # 记录已访问
                for i in range(len(word)):
                    for a in 'abcdefghijklmnopqrstuvwxyz':
                        new = word[:i] + a + word[i + 1:]
                        if new in backward:
                            if paths[0][0] == start_word: #回合路径是笛卡尔乘积
                                res.extend(fPath + bPath[::-1] for fPath in paths for bPath in backward[new])
                            else:
                                res.extend(bPath + fPath[::-1] for fPath in paths for bPath in backward[new])
                        if new in words and new not in visited:  # 仅当wordList存在该词且该词还未碰见过才进行BFS
                            tmp[new] = tmp.get(new, []) + [path + [new] for path in paths]
            _len += 1
            if res and _len > len(res[0]):  # res已有答案，且下一次BFS的会和路径长度已超过当前长度，不是最短
                break

            # 因为只遍历了前向，所以只更新前向
            forward = tmp
        return res
