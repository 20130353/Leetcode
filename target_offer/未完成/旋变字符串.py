# 答案错误:您提交的程序没有通过所有的测试用例
# case通过率为72.73%
# def solution(string, target):
#     if string.__len__() != target.__len__():
#         return False
#
#     if sorted(string) == sorted(target):
#         return True
#
#     return False

# 好像没有可以优化的方法！
# 内存超限:您的程序使用了超过限制的内存
# case通过率为9.09%
# 加入长度判断和sorted判断依然是超内存！

# 随时判断是否等于target
# 运行超时:您的程序未能在规定时间内运行结束，请检查是否循环有错或算法复杂度过大。
# case通过率为9.09%
# 要用DP

def get_change(string, target, flag):
    if flag[0]:
        return []

    if string.__len__() <= 1:
        return [string]

    if string.__len__() == 2:
        return [string, string[1] + string[0]]

    res = []
    for i in range(1, string.__len__()):
        left = string[:i]
        right = string[i:]
        change_left = get_change(left, target, flag)
        change_right = get_change(right, target, flag)

        # print('string {} left {},right {}'.format(string, left, right))
        # print('change_left {},change_right {}'.format(change_left, change_right))
        for i in range(len(change_right)):
            for j in range(len(change_left)):
                res.append(change_right[i] + change_left[j])
                res.append(change_left[j] + change_right[i])
                if target in res:
                    flag[0] = True
                    return res
    return res


def solution(string, target):
    if string.__len__() != target.__len__():
        return False
    if sorted(string) != sorted(target):
        return False
    if string == target:
        return True
    flag = [False]
    change_string = get_change(string, target, flag)
    return flag[0] or target in change_string


if __name__ == '__main__':
    string = input().strip()
    target = input().strip()
    ans = solution(string, target)  # soruce范围是100，target范围是100
    print('YES') if ans else print('NO')
