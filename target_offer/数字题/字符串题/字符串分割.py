# 出现的位置值少一，打印index数组看位置，挺方便的！
def solution(string, n):
    if n <= 1:
        return n

    dict = {}
    last_index = [0] * n
    for i in range(n - 1, -1, -1):
        if string[i] not in dict:
            dict[string[i]] = i
        last_index[i] = dict[string[i]]

    # print(last_index)
    # print(list(range(n)))
    ans = []
    pre_pos = 0
    max_last_index = -1
    for i in range(n):
        max_last_index = max(max_last_index, last_index[i])
        if max_last_index <= i:
            ans.append(str(i - pre_pos + 1))
            pre_pos = i + 1
    return ' '.join(ans)


if __name__ == '__main__':
    string = input().strip()
    ans = solution(string, string.__len__())
    print(ans)
