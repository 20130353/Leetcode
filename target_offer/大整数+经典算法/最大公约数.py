#
# 最大公约数：
# 1. 更损相减法
# 2.辗转相除法


# 更损相减法
# def solution(a, b):
#     while a != b:
#         if a > b:
#             a = a - b
#         else:
#             b = b - a
#     return a

# 辗转相除法
def solution(a, b):
    if a < b:
        a, b = b, a

    while b != 0:
        t = b
        a = a % b
        b = t
        if a < b:
            a, b = b, a
    return a


if __name__ == '__main__':
    ans = solution(1071, 462)
    print(ans)
