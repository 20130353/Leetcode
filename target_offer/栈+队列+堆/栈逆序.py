# -*- coding: utf-8 -*-
# Author: sunmengxin
# time: 10/23/18
# file: 栈逆序.py
# description:

'''
    只能用递归将栈反序
    解法1. 将首尾元素对调
    解法2. 将尾元素放到最上面
'''

# 解法一
def reverse(stack,low,high):

    if low >= high:
        return

    stack[low],stack[high] = stack[high],stack[low]
    reverse(stack,low+1,high-1)

def get_last(stack):
    if len(stack) == 1:
        res = stack[-1]
        del stack[-1]
        return res,stack
    else:
        last,new_stack = get_last(stack[:-1])
        new_stack.append(stack[-1])
        return last,new_stack

def reverse_2(stack):
    if len(stack) <= 0:
        return stack
    else:
        last,stack =  get_last(stack)
        new_stack = reverse_2(stack)
        new_stack.append(last)
        return new_stack



if __name__ == '__main__':
    stack = [1,2,3,4,5]
    # reverse(stack,0,len(stack)-1)
    res = reverse_2(stack)
    print(res)
