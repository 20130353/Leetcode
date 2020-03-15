# -*- coding: utf-8 -*-
# @File    : 合法括号序列判断.py
# @Author  : smx
# @Date    : 2019/10/14 
# @Desc    :

class Parenthesis:
    def chkParenthesis(self, string, n):
        if n & 1 == 1:
            return False
        num = 0
        for i in range(n):
            if string[i] == '(':
                num += 1
            elif string[i] == ')':
                num -= 1
                if num < 0:
                    return False
            else:
                return False
        return True if num == 0 else False


if __name__ == '__main__':
    string = input().strip()
    ans = Parenthesis().chkParenthesis(string, len(string))
    print(ans)
