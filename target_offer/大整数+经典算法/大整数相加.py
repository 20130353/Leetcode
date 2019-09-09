def solution(a, b):
    max_value = 1000000

    if a < max_value and b < max_value:
        print(a + b)

    a, b = str(a), str(b)
    print(a, b)
    if len(a) > len(b):
        for _ in range(len(a) - len(b)):
            b = '0' + b
    if len(b) > len(a):
        for _ in range(len(b) - len(a)):
            a = '0' + a

    flag = 0
    ans = ''
    for i in range(len(a) - 1, -1, -1):
        cur = int(a[i]) + int(b[i]) + flag
        if cur > 9:
            flag = 1
            ans = str(cur - 10) + ans
        else:
            flag = 0
            ans = str(cur) + ans
    if flag == 1:
        ans = '1' + ans
    print(ans)


# 1. 考虑string加法，补齐，从末尾开始加，如果进位就flag，
# 2. 打印string，从第一个非0位开始打印,这部不需要了，因为每加一位都是加到头上，所以不需要
# 注意考虑补位是补在开始的位置


if __name__ == '__main__':
    a, b = 100000000000000000000000, 444444444444444
    # a, b = 1000, 1000
    # a, b = 10000000000000000, 20

    solution(a, b)
