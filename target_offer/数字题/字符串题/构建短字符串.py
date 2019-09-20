# 出现的位置值少一，打印index数组看位置，挺方便的！
def solution(string, n, target):
    for i in range(n):
        if string[i] in target:
            pos = target.index(string[i])  # 必须要存在！
            target = target[:pos] + target[pos + 1:]
        else:
            return 'false'
    return 'true'


if __name__ == '__main__':
    source, target = input().strip().split(' ')
    ans = solution(source, source.__len__(), target)
    print(ans)

# aaa bababa
