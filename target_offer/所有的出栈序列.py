# -*- coding: utf-8 -*-
# Author: sunmengxin
# time: 10/23/18
# file: 所有的出栈序列.py
# description:
'''
    用递归+回溯的方式 模拟出栈和入栈
'''

def fun(stack,output,origin):
    if len(stack) == 0 and len(origin) == 0:
        print(output)
    elif len(stack) and len(output):
        # 出栈
        top = stack.pop()
        output.append(top)
        fun(stack,output,origin)
        stack.append(output.pop()) #恢复现场

        # 入栈
        stack.append(origin.pop())
        fun(stack,output,origin)
        origin.append(stack.pop()) #恢复现场

    elif len(stack) and len(origin) == 0:
        output.append(stack.pop())
        fun(stack,output,origin)
        stack.append(output.pop())# 恢复现场

    elif len(stack) == 0 and len(origin):
        stack.append(origin.pop())
        fun(stack,output,origin)
        origin.append(stack.pop()) # 恢复现场

if __name__ == '__main__':
    stack = [1,2,3]
    fun(stack,[],[])