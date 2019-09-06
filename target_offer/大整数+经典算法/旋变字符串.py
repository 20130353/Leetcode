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
def get_change(string):
    if string.__len__() <= 1:
        return [string]

    res = []
    for i in range(1, string.__len__()):
        left = string[:i]
        right = string[i:]
        change_left = get_change(left)
        change_right = get_change(right)

        # print('string {} left {},right {}'.format(string, left, right))
        # print('change_left {},change_right {}'.format(change_left, change_right))
        for i in range(len(change_right)):
            for j in range(len(change_left)):
                res.append(change_right[i] + change_left[j])
                res.append(change_left[j] + change_right[i])
    return res


def solution(string, target):
    if string.__len__() != target.__len__():
        return False
    change_string = get_change(string)
    # print(change_string)
    return target in change_string


if __name__ == '__main__':
    string = input().strip()
    target = input().strip()
    ans = solution(string, target)
    print('YES') if ans else print('NO')
