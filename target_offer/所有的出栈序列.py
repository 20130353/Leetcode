# -*- coding: utf-8 -*-
# Author: sunmengxin
# time: 10/23/18
# file: 所有的出栈序列.py
# description:
'''
    用递归+回溯的方式 模拟出栈和入栈
'''

import copy as cp


def fun(data, output, stack):
    # print('data', data)
    # print('output', output)
    # print('stack', stack)
    # print()

    # 数据已经全部进栈了,有全部从栈中输出,打印输出栈
    if len(data) == 0 and len(stack) == 0:
        print(output)

    # 所有数据全部进栈,只能出栈
    elif len(data) == 0 and len(stack) != 0:
        output.append(stack.pop())
        fun(data, output, stack)
        stack.append(output.pop())

    # 初始数据没有进栈,只能进栈
    elif len(data) and len(stack) == 0:
        stack.append(data.pop())
        fun(data, output, stack)

    # 数据没有全部进栈,可以选择出栈或者入栈
    elif len(data) and len(stack):
        # 入栈
        top = data.pop()
        stack.append(top)
        fun(data, output, stack)
        data.append(stack.pop())  # 恢复现场

        # 出栈
        output.append(stack.pop())
        fun(data, output, stack)
        stack.append(output.pop())  # 恢复现场


if __name__ == '__main__':
    data = [1, 2, 3]
    fun(data, [], [])


    '''
    正确答案:
    [ 3 2 1 ] 
    [ 2 3 1 ] 
    [ 2 1 3 ] 
    [ 1 3 2 ] 
    [ 1 2 3 ]
    
    '''
