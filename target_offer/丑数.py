# -*- coding: utf-8 -*-
# Author: sunmengxin
# time: 10/20/18
# file: 丑数.py
# description:
'''
    只包含因子2,3,5的数字叫做丑数求从小到达顺序的第1500个丑数
    解法1. 无限找每个数字.数字每次上加1,直到找个第1500个丑数
    解法2. 考虑丑数的全排列,用map或者set排除多余的丑数,然后排序得到第1500个
    解法3. 只考虑下一个丑数,直到1500个
    这里实现第三种解法
'''

def solution(index):
    if index == None or index <= 0:
        return 0
    num = [1 for _ in range(index)]
    next_index = 1
    index2 = 0
    index3 = 0
    index5 = 0
    while next_index < index:
        min_v = min([num[index2]*2,num[index3]*3,num[index5]*5])
        num[next_index] = min_v
        while num[index2] * 2 <= min_v:
            index2 += 1
        while num[index3] * 3 <= min_v:
            index3 += 1
        while num[index5] * 5 <= min_v:
            index5 += 1
        next_index += 1
    return num[-1]

if __name__ == '__main__':

    res = solution(9)
    print('第1500个丑数是:',res)
