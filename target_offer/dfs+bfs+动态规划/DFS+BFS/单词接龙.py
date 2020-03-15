#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 单词接龙.py
# @Author: smx
# @Date  : 2020/2/21
# @Desc  :

# 超时！19 / 40 个通过测试用例
# 找最短路径，如果使用DFS结果搜索时间太长，所以使用BFS

# 队列弹出方式不对！19 / 40 个通过测试用例
# 超时！29 / 40 个通过测试用例
# matrix 换成map,遍历的节点少一点！

# 33 / 40 个通过测试用例 双端队列
# 预处理时间太长！有些没有用到的节点都提前处理好了！

# index 花费太长时间

# 效率方式：set>map>list

from collections import deque

# 可以用深度优先遍历或者是广度优先遍历，还是可以双向深度或者广度优先遍历
class Solution:
    def ladderLength(self, start_word, end_word, words):
        if not start_word or not end_word or not words: return 0
        words = set(words)
        if end_word not in words: return 0

        n = len(words)
        start_queue = deque([start_word])
        end_queue = deque([end_word])
        vis = set()
        count = 1
        while start_queue:
            new_queue = deque()
            if len(start_queue) > len(end_queue):
                start_queue, end_queue = end_queue, start_queue
            for _ in range(len(start_queue)):
                top = start_queue.popleft()
                vis.add(top)
                for i in range(n):
                    left, right = top[:i], top[i + 1:]
                    for char in "abcdefghijklmnopqrstuvwxyz":
                        new_word = left + char + right
                        if new_word in end_queue:
                            return count + 1
                        if new_word in words and new_word not in vis:
                            new_queue.append(new_word)
            count += 1
            start_queue = new_queue
        return 0


if __name__ == '__main__':
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

    print(Solution().ladderLength(beginWord, endWord, wordList))
