# -*- coding: utf-8 -*-
# Author: sunmengxin
# time: 10/14/18
# file: 包含min函数的栈.py
# description:

'''
    栈中必须包含min,push和pop函数
'''

class stack:
    def __init__(self):
        self.data = []
        self.min_data = []
        self.min_key = None

    def add(self,key):
        self.data.append(key)
        self.min_data_add(key)


    def pop(self):
        self.data.pop()

    def min(self):
        if self.min_data == None or len(self.min_data) == 0:
            return None
        key = self.min_data.pop()
        return key

    def min_data_add(self,key):
        if self.min_key == None:
            self.min_key = key
            self.min_data.append(key)
        else:
            if self.min_key <= self.min_data[-1]:
                self.min_data.append(self.min_key)
            else:
                self.min_data.append(key)
                self.min_key = key
        return


if __name__ == '__main__':

    # data = [1,5,7,6,9]
    # data = []
    # data = [1]
    #

    s = stack()
    for each in data:
        s.add(each)
    print(s.min())


