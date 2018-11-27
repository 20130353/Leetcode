# -*- coding: utf-8 -*-
# author: sunmengxin
# time: 18-11-26
# file: 字符串的模式匹配
# description:


# 反思:
# 1. 值得肯定的是我刚开始做出来了一部分,但是缺点是我对于*
# 能考虑的状况少了一部分,这个以后要注意!
# 2. 数组索引的时候一定要看好索引大小,防止越界

class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):
        # write code here
        if len(s) == 0 and len(pattern) == 0:
            return True
        if len(s) > 0 and len(pattern) == 0:
            return False
        if len(s) == 0 and len(pattern) > 0:
            return False

        # 这段代码有问题
        j = 0
        for inx, each in enumerate(pattern):
            if each != '.' and each != '*' and each == s[j]:
                j += 1
            elif each == '.':
                continue
            elif each == '*':
                sub_len = len(pattern[inx + 1])
                if j + 1 + sub_len < len(s):
                    sub = s[j + 1 + sub_len]
                    check = sum([0 if e == pattern[inx - 1] else 1 for e in sub])
                    if check > 0:
                        return False
                    else:
                        j = j + 1 + sub_len
            else:
                return False
        if j == len(s) - 1:
            return True
        else:
            return False


class Solution:

    def match(self, s, pattern):

        if len(s) == 0 and len(pattern) == 0:
            return True

        # 这一段是错误的!
        # 因为当字符串已经为空,但是模式串不为空的时候,可能会存在匹配成功的情况
        # if len(s) == 0 and len(pattern) != 0:
        #     return False
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
