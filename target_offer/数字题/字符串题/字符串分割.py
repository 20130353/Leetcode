# 出现的位置值少一，打印index数组看位置，挺方便的！
# 给定一个由小写字母组成的字符串s，请将其分割成尽量多的子串，
# 并保证每个字母最多只在其中一个子串中出现。请返回由一个或多个整数表示的分割后各子串的长度。
def solution(string, n):
    if n <= 1:
        return n

    # 记录最后一个元素出现的位置
    dict = {}
    for i in range(len(string)):
        dict[string[i]] = i

    ans = []
    pre_pos = 0
    max_last_index = -1
    for i in range(n):
        max_last_index = max(max_last_index, dict[string[i]])
        if max_last_index <= i:
            ans.append(str(i - pre_pos + 1))
            pre_pos = i + 1
    return ' '.join(ans)


if __name__ == '__main__':
    string = input().strip()
    ans = solution(string, string.__len__())
    print(ans)
