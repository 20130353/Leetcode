# -*- coding:utf-8 -*-
# 答案错误:您提交的程序没有通过所有的测试用例
# case通过率为20.00%

# 这道题目的意思是：只要是4全顺子或全刻字或顺子和刻字交叠就行！
# 用递归遍历所有的情况即可！
# 出现的问题：只遍历一种情况结果遍历

# 这道题刚开始觉得很麻烦，不想做！
# 出现的问题：自己找不到错误的case!
# AC

import copy as cp


def solution(arr):
    def is_hu(arr, flag):
        if not arr or arr.__len__() <= 0:
            return flag[0]

        counter = arr.count(arr[0])
        if counter >= 3 and is_hu(arr[3:], flag):
            return True

        if counter >= 2 and flag[0] is False:
            flag = [True]
            if is_hu(arr[2:], flag):
                return True
            flag = [False]

        if arr[0] + 1 in arr and arr[0] + 2 in arr:
            temp = cp.deepcopy(arr)
            temp.remove(arr[0])
            temp.remove(arr[0] + 1)
            temp.remove(arr[0] + 2)
            if is_hu(temp, flag):
                return True
        return False

    ans = []
    for i in range(1, 10):
        if arr.count(i) <= 3:
            temp = arr + [i]
            temp.sort()
            if is_hu(temp, [False]):
                ans.append(str(i))
    return ans


if __name__ == '__main__':
    # arr = [1, 1, 1, 2, 2, 2, 5, 5, 5, 6, 6, 6, 9]
    # --> 9
    # arr = [1, 1, 1, 1, 2, 2, 3, 3, 5, 6, 7, 8, 9]
    # --> 4 7
    # arr = [1, 1, 1, 2, 2, 2, 3, 3, 3, 5, 7, 7, 9]
    # --> 0
    # arr = [1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 9]
    # --> 8

    arr = list(map(int, input().strip().split(' ')))
    ans = solution(arr)
    print(' '.join(ans)) if ans.__len__() > 0 else print(0)
