# -*- coding: utf-8 -*-
# author: sunmengxin
# time: 18-11-15
# file: 两个栈完成一个队列
# description:

# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, node):
        self.stack1.append(node)

        # write code here


    # 这份代码存在的问题是：还要把stack2中的元素重新放回去，其实是没有必要的
    # def pop(self):
    #     # return xx
    #     self.stack2 = []
    #     if self.stack1 == []:
    #         return None
    #
    #     while len(self.stack1) > 1:
    #         self.stack2.append(self.stack1.pop())
    #
    #     res = self.stack1.pop()
    #
    #     while self.stack2:
    #         self.stack1.append(self.stack2.pop())
    #
    #     return res

    # 这份代码存在的问题是没有想到stack1可能为空
    # def pop(self):
    #     # return xx
    #     if self.stack2 == []:
    #         while len(self.stack1):
    #             self.stack2.append(self.stack1.pop())
    #         return self.stack2.pop()
    #     return  self.stack1.pop()

    def pop(self):
        # return xx
        if self.stack1 == [] and self.stack2 == []:
            return None

        if self.stack2 == []:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            return self.stack2.pop()
        return  self.stack1.pop()



