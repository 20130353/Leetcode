# -*- coding: utf-8 -*-
# Author: sunmengxin
# time: 10/20/18
# file: x 出现的数目.py
# description:
'''
    给定一个数字n,m,求从1到n出现的m的次数
    1. 对每个数字求一遍出现m的次数,最后累加
    2. 直接计算数字的规律
    这里实现第二种解法
'''

import math

def solution(n,x):

    if n < 0 or x < 0 or x > 9:
        return 0

    tmp = n
    bits = 0
    while tmp:
        tmp //= 10
        bits += 1

    total = 0
    for i in range(1,bits+1):
        high = n//math.pow(10,i)
        low = (n%math.pow(10,i))%math.pow(10,i-1)
        cut = (n//math.pow(10,i-1)) - (n//math.pow(10,i))*10
        if cut == x:
            total += high * math.pow(10,i-1) + low + 1
        elif cut < x:
            total += high * math.pow(10,i-1)
        else:
            total += (high+1) * math.pow(10,i-1)

        # print(total,end='\t')
    return total

if __name__ == '__main__':

    count = solution(2593,5)
    print(count)

    # print(259+260+294)




