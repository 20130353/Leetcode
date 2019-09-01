# -*- coding: utf-8 -*-
# Author: sunmengxin
# time: 10/10/18
# file: 用两个栈实现队列.py
# description:


import numpy as np

class Queue:
    def __init__(self):
        self.stack = []
        self.new_stack = []

    def add(self,data):
        self.stack.append(data)
        return

    def delhead(self):

        if len(self.stack) == 0:
            return

        self.new_stack = []
        for _ in range(len(self.stack)-1):
            self.new_stack.append(self.stack.pop())

        del_data = self.stack.pop()
        print('delete data is ',del_data)

        for _ in range(len(self.new_stack)):
            self.stack.append(self.new_stack.pop())

        return



if __name__ == '__main__':

    data = [1,3,4,6,7,8]
    queue = Queue()
    for each in data:
        queue.add(each)

    for _ in range(len(data)):
        queue.delhead()


