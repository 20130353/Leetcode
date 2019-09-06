def solution(string, target):
    i, j, start = 0, 0, 0
    while i < string.__len__():
        if string[i] == target[j]:
            if j == 0:
                start = i
            i += 1
            j += 1
            if j == target.__len__():
                return i - start
        else:
            i += 1
    return 0


if __name__ == '__main__':
    string = input().strip()
    target = input().strip()
    ans = solution(string, target)
    print(ans)


# 423141234578909
# 1239