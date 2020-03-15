# -*- coding: utf-8 -*-
# @File    : 翻转字符串2.py
# @Author  : smx
# @Date    : 2019/10/14 
# @Desc    :


if __name__ == '__main__':
    size = int(input().strip())
    string = input().strip()
    ans = ''.join(string[size:] + string[:size])
    print(ans)
