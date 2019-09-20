# 出现的问题：超时--》30%
# 改成公式
# AC

if __name__ == '__main__':
    n, m = map(int, input().strip().split(' '))

    ans = 0
    flag, count = -1, 0
    for i in range(1, 2 * m + 1):
        count += 1
        ans += flag * i
        if count == m:
            flag *= (-1)
            count = 0

    ans = ans * (n / (2 * m))
    print(int(ans))
