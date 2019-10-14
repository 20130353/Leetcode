# -*- coding: utf-8 -*-
# @File    : 完成括号匹配.py
# @Author  : smx
# @Date    : 2019/10/14 
# @Desc    :

# 这种方式没有办法找到括号序列！
# 可以找到，我想到的问题存在！
# 但是可以通过加左右两个部分解决！
def solution(string):
    num = 0
    pre = ''
    for i in range(len(string)):
        if string[i] == '[':
            num += 1
        else:
            num -= 1
            if num < 0:
                pre = '[' + pre
                num = 0
    while num > 0:
        string += ']'
        num -= 1
    return pre + string


if __name__ == '__main__':
    string = input().strip()
    ans = solution(string)
    print(ans)
