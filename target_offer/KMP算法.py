# -*- coding: utf-8 -*-
# author: sunmengxin
# time: 18-11-26
# file: KMP算法
# description:

class KMP:

    def prefix_table(self, pattern, n):

        prefix = [0 for _ in range(n)]
        len = 0  # 之前匹配的字符的长度
        i = 1
        while i < n:
            if pattern[i] == pattern[len]:  # 之前已经匹配的长度的后一个字符和现在看的这个字符是是否一样的(这个字符本身就是当前的后缀的最后一个字符)
                len += 1
                prefix[i] = len
                i += 1
            else:
                if len > 0:
                    len = prefix[len - 1]  # 斜着对
                else:
                    prefix[i] = len  # 对到第一个字符了,之前没有字符可以继续对了
                    i += 1

        #     将整个prefixtable向后一位,首位是-1
        prefix.insert(0, -1)
        return prefix

    def kmp(self, text, pattern):

        n, m = len(pattern), len(text)
        prefix = self.prefix_table(pattern, n)
        i, j = 0, 0
        while i < m:  # 从头开始找,一直找到结尾
            if j == n:
                print('found at', i - j)
                j = prefix[j]
            if text[i] == pattern[j]:
                i += 1
                j += 1
            else:
                j = prefix[j]
                if j == -1:  # 找到最末尾的地方,依然无法匹配只能都向后移动,重新开始匹配
                    i += 1
                    j += 1
        return


if __name__ == '__main__':
    pattern = 'ABABA'
    text = 'AAAABABABABACC'
    KMP = KMP()
    print(KMP.kmp(text, pattern))
