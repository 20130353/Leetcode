# 运行超时:您的程序未能在规定时间内运行结束，请检查是否循环有错或算法复杂度过大。
# case通过率为40.00%
# 少考虑了不相等，但是a*的情况

# 运行超时:您的程序未能在规定时间内运行结束，请检查是否循环有错或算法复杂度过大。
# case通过率为85.00%


# 运行超时:您的程序未能在规定时间内运行结束，请检查是否循环有错或算法复杂度过大。
# case通过率为65.00%
# def solution(string, pattern):
#     if string.__len__() == 0:
#         if pattern == '*':
#             return True
#         return pattern.__len__() == 0
#
#     if len(pattern) >= 2 and pattern[1] == '*':
#         return solution(string[1:], pattern) or solution(string[1:], pattern[2:])
#     else:
#         if string[0] == pattern[0] or pattern[0] == '.':
#             return solution(string[1:], pattern[1:])
#         else:
#             return False


# 这个代码写的非常棒！
# 运行超时:您的程序未能在规定时间内运行结束，请检查是否循环有错或算法复杂度过大。
# case通过率为65.00%
def solution(string, pattern):
    if string.__len__() == 0:
        return pattern.__len__() == 0

    first_match = pattern.__len__() != 0 and (string[0] == pattern[0] or pattern[0] == '.')
    if pattern.__len__() >= 2 and pattern[1] == '*':
        return solution(string[1:], pattern[2:]) or (first_match and solution(string[1:], pattern))
    else:
        return first_match and solution(string[1:], pattern[1:])


if __name__ == '__main__':
    string = input().strip()
    pattern = input().strip()
    ans = solution(string, pattern)
    print('YES') if ans else print('NO')

# fasfadasfa
# # ..*sfada...
