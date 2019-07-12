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
            cn += 1
            next.append(cn)
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

    
# 对应的练习题, 给定一个字符串,求最小的无重复子串, 要求子串能通过n次拼接得到原来的字符串
# 解题关键是: 给字符串增加一个字符,求它的next数组, 最后的next数组值就是子串的长度
def get_min_substr(str):
    next = get_next(str + '#')
    return next[-1], str[:next[-1]]
 
    
# 对应的练习题: 给一个字符串, 求2个字符串拼接后去掉相连的字符的长度
def get_min_str(str):
    next = get_next(str + '#')
    return 2 * len(str) - next[-1]


if __name__ == '__main__':
    str1, str2 = '45102345', '123'
    ans = KMP(str1, str2)
    print(ans)
    
    
    str = 'abcabc'
    ans = get_min_substr(str)
    print(ans)
    
    str = 'abca'
    ans = get_min_str(str)
    print(ans)

