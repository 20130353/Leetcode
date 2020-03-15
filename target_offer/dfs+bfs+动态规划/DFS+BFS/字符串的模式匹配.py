# -*- coding: utf-8 -*-
# author: sunmengxin
# time: 18-11-26
# file: 字符串的模式匹配
# description:


# 虽然写的有些啰嗦，但是也是全对的，可以重点看一下case！
class Solution:
    def dfs(self, i, j, s, pat, flag):
        if flag[0]:
            return
        if i >= len(s) and j >= len(pat):
            flag[0] = True
            return
        if j >= len(pat) and i < len(s):
            return

        # 这两段可以合并！--》没有必要把这个情况写出来！
        if pat[j] == '.' and j + 1 < len(pat) and pat[j + 1] == '*':
            self.dfs(i, j + 2, s, pat, flag)
            if flag[0]:
                return
            # 这一段可以写成不去掉*
            for k in range(len(s) - i + 1):
                self.dfs(i + k, j + 2, s, pat, flag)
                if flag[0]:
                    return

        if j + 1 < len(pat) and pat[j + 1] == '*':
            if i < len(s):
                self.dfs(i, j + 2, s, pat, flag)
                if s[i] == pat[j]:
                    while s[i] == pat[j]:
                        self.dfs(i + 1, j + 2, s, pat, flag)
                        if flag[0]:
                            return
                        i = i + 1
            else:
                self.dfs(i, j + 2, s, pat, flag)

        if (i < len(s) and pat[j] == '.') or (i < len(s) and s[i] == pat[j]):
            self.dfs(i + 1, j + 1, s, pat, flag)

    def match(self, s, pattern):
        flag = [False]
        self.dfs(0, 0, s, pattern, flag)
        return flag[0]


# 反思:
# 1. 值得肯定的是我刚开始做出来了一部分,但是缺点是我对于*能考虑的状况少了一部分,这个以后要注意!
# 2. 数组索引的时候一定要看好索引大小,防止越界
class Solution:
    def match(self, s, pattern):
        if len(s) == 0 and len(pattern) == 0:
            return True

        if len(s) != 0 and len(pattern) == 0:
            return False

        if len(pattern) > 1 and pattern[1] == '*':
            if len(s) > 0 and (s[0] == pattern[0] or pattern[0] == '.'):
                return self.match(s, pattern[2:]) or self.match(s[1:], pattern[2:]) or self.match(s[1:], pattern)
            else:
                return self.match(s, pattern[2:])

        if len(s) > 0 and (pattern[0] == '.' or s[0] == pattern[0]):
            return self.match(s[1:], pattern[1:])

        return False


if __name__ == '__main__':
    so = Solution()
    print(so.match('aaa', 'a.a'))  # True
    print(so.match('aaa', 'a*a'))  # True
    print(so.match('aaa', 'ab*ac*a'))  # True
    print(so.match('aaa', 'aa.a'))  # False
    print(so.match('aaa', 'ab*a'))  # False
    print(so.match(',', '.*'))  # True
