# -*- coding: utf-8 -*-
# Author: sunmengxin
# time: 10/14/18
# file: 栈的压入和弹出序列.py
# description:

'''
    给定一个入栈序列和出栈序列,判断出栈序列顺序是否正确
'''

def judge(in_stack,out_stack):

    stack = []
    for each in out_stack:
        if each in in_stack:
            inx = in_stack.index(each)
            for e in in_stack[:inx]:
                stack.append(e)
                in_stack.remove(e)
            in_stack.remove(each)
        else:
            stack_top = stack.pop()
            if stack_top != each:
                return False
    return True

if __name__ == '__main__':
    in_stack = [1, 2, 3, 4, 5]
    # out_stack = [4, 5, 3, 2, 1]
    out_stack = [4,3,5,1,2]

    print(judge(in_stack, out_stack))


