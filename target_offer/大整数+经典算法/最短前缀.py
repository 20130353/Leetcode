# -*- coding: utf-8 -*-
# @File    : 最短前缀.py
# @Author  : smx
# @Date    : 2019/10/14 
# @Desc    :
# 格式问题没有解决！

class Node:
    def __init__(self):
        self.data = {}
        self.is_word = False
        self.num = 0


# 找前缀树重点是要标记每个字符出现的次数！
class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, string):
        node = self.root
        for ch in string:
            if node.data.get(ch) is None:
                node.data[ch] = Node()
            node.num += 1
            node = node.data[ch]
        node.is_word = True

    def search(self, string):
        # 最短前缀就是中间或者整个字符串，中间停止是只出现一次
        node = self.root
        i = 0
        ans = ''
        while i < len(string) and node.num != 1:
            ans += string[i]
            node = node.data[string[i]]
            i += 1
        return string if i == len(string) else ans

    def solution(self, strings):
        sorted_s = sorted(strings)
        ans = {}
        for each in sorted_s:
            ans[each] = self.search(each)
        return ans


if __name__ == '__main__':
    import sys

    lines = sys.stdin.readlines()
    i = 0
    while i < len(lines):
        n = int(lines[i])
        strings = lines[i + 1:i + n + 1]
        i = i + n + 1
        T = Trie()
        for j in range(n):
            T.insert(strings[j])
        ans = T.solution(strings)
        for j, each in enumerate(strings):
            if j < len(strings) - 1:
                print(ans[each])
            else:
                if i < len(lines):
                    print(ans[each] + '\n')
                else:
                    print(ans[each])
