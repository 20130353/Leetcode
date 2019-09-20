class Machine:
    def __init__(self, time, level):
        self.time = time
        self.level = level


class Task:
    def __init__(self, time, level):
        self.time = time
        self.level = level


# 如果做不出来直接暴力循环或者模拟!
# 答案错误:您提交的程序没有通过所有的测试用例
# case通过率为30.00%

# 用贪心算法，每次为每个机器找到收益最大的任务
# 没有考虑最大收益和每个机器是否能完成任务的时间限制
# 答案错误:您提交的程序没有通过所有的测试用例
# case通过率为40.00%

# 可能获取的是最大收益但不是完成了最多的任务数量！
# 解决方案：
# 小机器做长时间任务！
# 小机器做大难度任务！

# 答案错误:您提交的程序没有通过所有的测试用例
# case通过率为60.00%
# 存在的问题：不能得到最大收益！

# 还是过不了最长的那个例子！
# 解决方案
# 对符合时间条件的job选择最接近的level

# 这里有两种考虑：时间最接近，level最接近和二者的绝对值差值最接近

# def solution(task, machine, task_num, machine_num):
#     # 这里排序可以按照两个属性排序
#     task.sort(key=lambda x: x.time)
#     machine.sort(key=lambda x: x.level)
#
#     vis = [0] * task_num
#     total_task, total_profit = 0, 0
#
#     for i in range(machine_num):
#         max_j, max_use = -1, -1
#         for j in range(task_num - 1, -1, -1):
#             if vis[j] == 0 and machine[i].level >= task[j].level and machine[i].time >= task[j].time:
#                 cur_use = machine[i].time - task[j].time + machine[i].level - task[j].level
#                 if max_use == -1 or cur_use < max_use:
#                     max_j = j
#                     max_use = cur_use
#         if max_j != -1:
#             vis[max_j] = 1
#             total_task += 1
#             total_profit += 200 * task[max_j].time + 3 * task[max_j].level
#
#     return total_task, total_profit


def solution(task, machine, task_num, machine_num):
    task.sort(key=lambda x: (x.time, x.level), reverse=True)
    machine.sort(key=lambda x: (x.time, x.level), reverse=True)

    # print('task:', [(each.time, each.level) for each in task])
    # print('machine:', [(each.time, each.level) for each in machine])

    profit = 0
    #  这里用level++的方式真是非常奇妙了!
    level = [0] * 101
    count = 0
    j = 0
    for t in task:
        # 这里可以避免二次消耗！
        # 因为目标是找到>tasktime且level的机器，需要两个for循环，n*m复杂度。
        # 但是多用了一个数组,就只需要m+n的复杂度!
        while j < machine_num and machine[j].time >= t.time:
            level[machine[j].level] += 1
            j += 1
        for i in range(t.level, 101):
            if level[i] > 0:
                count += 1
                level[i] -= 1
                profit += 200 * t.time + 3 * t.level
                break
    return count, profit


if __name__ == '__main__':
    machine_num, task_num = map(int, input().strip().split(' '))
    machine, task = [], []

    for i in range(machine_num):
        max_time, level = map(int, input().strip().split(' '))
        machine.append(Machine(max_time, level))

    for i in range(task_num):
        max_time, level = map(int, input().strip().split(' '))
        task.append(Task(max_time, level))

    ans = solution(task, machine, task_num, machine_num)

    print(' '.join(map(str, ans)))
