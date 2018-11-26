# -*- coding: utf-8 -*-
# author: sunmengxin
# time: 18-11-26
# file: 字符串转换成数字（不能使用库函数）
# description:

# class Solution:
#     def StrToInt(self, s):
#         # write code here
#
#         import unicodedata
#         try:
#             # 这是调用库函数的方式
#             unicodedata.numeric(s)
#             return True
#         except Exception:
#             return False


# 反思:
# 1. 刚开始不知道怎么做,就应该想到一个一个元素判断.最基本的方法就是一个一个元素的判断
# 2. 没有考虑到正负数。对于数字题一定要考虑正负数
# 3. 基础的考虑应该写到try,catch
class Solution:

    def char2int(self, ch):
        dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 0}
        return dict.get(ch)

    def multi_int(self, x, y):
        return 10 * x + y

    def StrToInt(self, s):

        from functools import reduce
        if not s:
            return 0

        flag = False
        if s[0] == '-':
            s = s[1:]
            flag = True
        elif s[0] == '+':
            s = s[1:]

        if s.find('.') == -1:
            try:
                ans = reduce(self.multi_int, map(self.char2int, s))
            except Exception:
                return 0
            else:
                return ans if not flag else -ans
        else:
            ss = s.split('.')
            try:
                ssint = reduce(self.multi_int, map(self.char2int, ss[0]))  # 整数部分
                ssfloat = reduce(self.multi_int, map(self.char2int, ss[1])) * 0.1 ** len(ss[1])  # 小数部分
            except:
                return 0
            else:
                return ssint + ssfloat if not flag else -(ssint + ssfloat)

if __name__ == '__main__':

    so = Solution()
    print(so.StrToInt('123'))
    print(so.StrToInt('123.456'))
    print(so.StrToInt('abc'))
    print(so.StrToInt('+123'))
    print(so.StrToInt('-123'))
    print(so.StrToInt('-123.343'))
