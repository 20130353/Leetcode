def get_next(str):
    if len(str) == 1:
        return [-1]

    if len(str) == 2:
        return [-1, 0]

    next = [-1, 0]
    cn = 0
    i = 2
    while i < len(str):
        if str[i - 1] == str[cn]:
            next[i] = cn + 1
            i += 1
        elif cn > 0:
            cn = next[cn]
        else:
            next.append(0)
            i += 1
    return next


def KMP(str1, str2):
    i, j = 0, 0
    next = get_next(str2)
    while i < len(str1) and j < len(str2):
        if str1[i] == str2[j]:
            i += 1
            j += 1
        else:
            if next[j] == -1:
                i += 1
            else:
                j = next[j]

    if j == len(str2):
        return True, i - j
    else:
        return False, -1


if __name__ == '__main__':
    str1, str2 = '45102345', '123'
    ans = KMP(str1, str2)
    print(ans)
