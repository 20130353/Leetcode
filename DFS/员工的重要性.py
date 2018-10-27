# -*- coding: utf-8 -*-
# Author: sunmengxin
# time: 10/26/18
# file: 员工的重要性.py
# description:

'''
给定一个保存员工信息的数据结构，它包含了员工唯一的id，重要度 和 直系下属的id。

比如，员工1是员工2的领导，员工2是员工3的领导。他们相应的重要度为15, 10, 5。那么员工1的数据结构是[1, 15, [2]]，员工2的数据结构是[2, 10, [3]]，员工3的数据结构是[3, 5, []]。注意虽然员工3也是员工1的一个下属，但是由于并不是直系下属，因此没有体现在员工1的数据结构中。

现在输入一个公司的所有员工信息，以及单个员工id，返回这个员工和他所有下属的重要度之和。

示例 1:

输入: [[1, 5, [2, 3]], [2, 3, []], [3, 3, []]], 1
输出: 11
解释:
员工1自身的重要度是5，他有两个直系下属2和3，而且2和3的重要度均为3。因此员工1的总重要度是 5 + 3 + 3 = 11。
'''

def get_importance(ob,dict):

    # print(ob)
    em_list = ob['em'].replace('[','').replace(']','').replace(',','')
    if len(em_list) == 0 or em_list == None or em_list == '':
        return int(ob['im'])
    else:
        sum = int(ob['im'])
        for each_id in em_list:
            print(each_id)
            print(dict[each_id])
            sum += get_importance(dict[each_id],dict)
        return sum

if __name__ == '__main__':

    dict = {}
    n = int(input().strip())
    for _ in range(n):
        id,im,em = input().split(' ')
        dict[id] = {'id':id,'im':im,'em':em}
    # print(dict)
    key = input().strip()
    for k,item in dict.items():
        if k == key:
            ans = get_importance(dict[k],dict)
            print('ans:',ans)
            break


'''
3
1 5 [2,3]
2 3 []
3 3 []
1

'''