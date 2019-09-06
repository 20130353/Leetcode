def get_next(string):
    next = [-1, 0]
    i = 2
    cnt = 0
    while i < len(string):
        if string[cnt] == string[i - 1]:
            cnt += 1
            next.append(cnt)
            i += 1
        elif cnt > 0:
            cnt = next[cnt]
        else:
            next.append(0)
            i += 1
    return next


def KMP(string, pattern):
    next = get_next(pattern)
    i, j = 0, 0
    match_start = []
    while i < len(string):
        if j == -1 or string[i] == pattern[j]:
            i += 1
            j += 1
            if j == len(pattern):
                match_start.append(i - j)
                j = 0 # 这里真的很奇怪！
        else:
            j = next[j]
    return match_start


if __name__ == '__main__':
    string = input().strip()
    pattern = input().strip()
    ans = KMP(string, pattern)
    print(' '.join(map(str, ans))) if len(ans) >= 1 else print(-1)
