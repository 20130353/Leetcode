# 答案错误:您提交的程序没有通过所有的测试用例
# case通过率为70.00%
# 出现的问题：可以不吃完！
# AC
import math


def cal_pred(first_day, day):
    pred_total = 0
    cur_day = first_day
    for i in range(day):
        pred_total += cur_day
        cur_day = math.ceil(cur_day / 2)
    return pred_total


def solution(day, total):
    if total == day:
        return 1
    if day == 1:
        return total

    # 用二分查找第一天可以吃的总量,这里可以没有吃完！
    low, high = 0, total
    while low < high:
        mid = low + (high - low + 1) // 2
        pred_total = cal_pred(mid, day)
        # print('low {},high {},mid {},pred_total {}'.format(low, high, mid, pred_total))
        if pred_total > total:
            high = mid - 1
        elif pred_total <= total:
            low = mid
    return low


if __name__ == '__main__':
    day, total = map(int, input().strip().split(' '))
    ans = solution(day, total)
    print(ans)
