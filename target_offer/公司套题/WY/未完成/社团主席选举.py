# # 答案错误:您提交的程序没有通过所有的测试用例
# # case通过率为20.00%
# # def solution():
# #     ans = 0
# #     while True:
# #         sorted_item = sorted(map_get.items(), key=lambda x: x[1])
# #         if sorted_item.__len__() >= 2:
# #             if sorted_item[-1][0] == 1 and sorted_item[-1][1] > sorted_item[-2][1]:
# #                 print(ans)
# #                 break
# #         else:
# #             if sorted_item[-1][0] == 1:
# #                 print(ans)
# #                 break
# #
# #         max_get = sorted_item[-1][1]
# #         min_value, max_i = float('inf'), -1
# #         for each in sorted_item:
# #             if each[0] != 1 and each[1] == max_get and (max_i == -1 or min(map_supporter[each[0]]) < min_value):
# #                 min_value = min(map_supporter[each[0]])
# #                 max_i = each[0]
# #
# #         ans += min_value
# #         map_supporter[max_i].remove(min_value)
# #         map_get[max_i] -= 1
# #         map_get[1] += 1
#
#
# # 思路存在问题：获胜的方法不一定是只能从其他得票最多的人那里争取支持者，也可以找普通的支持者。
# # 所以每次有两种选择：一种整体花费最少的支持者，一种其他最多得票的支持者！
# # 用DFS来做
# # 答案错误:您提交的程序没有通过所有的测试用例
# # case通过率为20.00%
# # 我的答案大了！
# # 应该是找支持者找的有问题！
# # 找不到，重新写一遍吧！
# # 奇怪！真是找不到为什么！
#
# # def dfs(get, supporter, cost, min_cost):
# #     sorted_get = sorted(get.items(), key=lambda x: x[1])
# #     if sorted_get[-1][0] == 1:
# #         if sorted_get.__len__() == 1 or (
# #                 sorted_get.__len__() >= 2 and sorted_get[-1][1] > sorted_get[-2][1]):
# #             print('sorted_get {}, cost {}'.format(sorted_get, cost))
# #             min_cost[0] = min(cost, min_cost[0])
# #             return
# #
# #     # if cost >= min_cost[0]:
# #     #     return
# #
# #     # 两种最小支持者
# #     max_get = sorted_get[-1][1]
# #     min_value, max_i = float('inf'), -1
# #     min_value1, max_i1 = float('inf'), -1
# #     for each in sorted_get:
# #         if each[0] != 1 and each[1] == max_get and (max_i == -1 or min(supporter[each[0]]) < min_value):
# #             min_value = min(supporter[each[0]])
# #             max_i = each[0]
# #
# #         if each[0] != 1 and len(supporter[each[0]]) >= 1 and (max_i1 == -1 or min(supporter[each[0]]) < min_value):
# #             min_value1 = min(supporter[each[0]])
# #             max_i1 = each[0]
# #
# #     print('其他得票者的最小支持者 {}'.format(min_value))
# #     print('最小支持者 {}'.format(min_value1))
# #
# #     # 选择其他最大支持者的最小支持者]
# #     if max_i != -1:
# #         supporter[max_i].remove(min_value)
# #         get[max_i] -= 1
# #         get[1] += 1
# #         dfs(get, supporter, cost + min_value, min_cost)
# #         # 还原
# #         supporter[max_i].append(min_value)
# #         get[max_i] += 1
# #         get[1] -= 1
# #
# #     # 如果是不同的最小者选择
# #     if max_i != max_i1 and max_i1 != -1:
# #         # 选择最小的支持者
# #         supporter[max_i1].remove(min_value1)
# #         get[max_i1] -= 1
# #         get[1] += 1
# #         dfs(get, supporter, cost + min_value1, min_cost)
# #         # 还原
# #         supporter[max_i1].append(min_value1)
# #         get[max_i1] += 1
# #         get[1] -= 1
# #
# #
# # if __name__ == '__main__':
# #     # 投票者和候选人
# #     n, m = map(int, input().strip().split(' '))
# #     arr = []
# #     get = {}
# #     supporter = {}
# #     for i in range(m):
# #         get[i + 1] = 0
# #         supporter[i + 1] = []
# #     for _ in range(n):
# #         data = list()
# #         get[data[0]] += 1
# #         supporter[data[0]].append(data[1])
# #         arr.append(data[1])
# #
# #     print('get {}'.format(get))
# #     for each in supporter.items():
# #         if each[1].__len__() >= 1:
# #             print(each)
# #     arr.sort()
# #     print(arr)
# #     min_cost = [float('inf')]
# #     dfs(get, supporter, 0, min_cost)
# #     print(min_cost[0])
#
from collections import Counter
# counter.most_common 返回的tuple

def max_candidate(arr):
    # 返回（候选人id）
    counter = Counter([each[0] for each in arr]).most_common(1)
    return counter[0][0]


def find_founder(arr, mcand):
    # 返回当前最大得票的最小支持者和普通的最小支持者，并判断两个是否是同一个
    minv1, minv2 = 0, 0
    for i in range(arr.__len__()):
        if arr[i][0] == mcand and arr[i][1] < arr[minv1][1]:
            minv1 = i
        if arr[i][1] < arr[minv2][1]:
            minv2 = i
    return (minv1, minv2) if minv1 != minv2 else (minv1, None)


def solution(arr, cost, min_cost):
    # 找到得票最大的候选人
    mcand = max_candidate(arr)
    if mcand == 1:
        min_cost[0] = min(min_cost[0], cost)
        return

    inx1, inx2 = find_founder(arr, mcand)

    # 选择其他最大支持者的最小支持者
    save_data = arr[inx1]
    arr.remove(arr[inx1])
    arr.append((1, save_data[1]))
    solution(arr, cost + save_data[1], min_cost)
    arr.append(save_data)

    # 如果是不同的最小者选择
    if inx2 is not None:
        save_data = arr[inx2]
        arr.remove(arr[inx2])
        arr.append((1, save_data[1]))
        solution(arr, cost + save_data[1], min_cost)
        arr.append(save_data)


if __name__ == '__main__':
    n, m = map(int, input().strip().split(' '))
    arr = []
    for i in range(n):
        a, b = map(int, input().strip().split(' '))
        arr.append((a, b))
    min_cost = [float('inf')]
    ans = solution(arr, 0, min_cost)
    print(min_cost[0])  
