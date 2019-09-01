# -*- coding: utf-8 -*-
# Author: sunmengxin
# time: 10/14/18
# file: 栈的压入和弹出序列.py
# description:

'''
    给定一个入栈序列和出栈序列,判断出栈序列顺序是否正确
'''

'''
    反思：
    1. 使用index和list[index]之前确保不是空
    

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


class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here

        if not pushV or not popV:
            return False

        stack = []
        for each in popV:
            if each in pushV:
                index = pushV.index(each)
                for _ in range(index):
                    stack.append(pushV[0])
                    del pushV[0]
                pushV.remove(each)
            elif stack and stack[-1] == each:
                stack.pop()
            else:
                return False
        if stack:
            return False
        else:
            return True


if __name__ == '__main__':
    in_stack = [1, 2, 3, 4, 5]
    # out_stack = [4, 5, 3, 2, 1]
    out_stack = [4,3,5,1,2]

    # print(Solution().IsPopOrder([1], [2]))
    print([1,2,3].pop(0))


