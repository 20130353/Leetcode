def get_next(string):
    '''
    普通的next数组不需要添加#，但是字符串拼接需要计算到最后一个字符的最长前缀和最长后缀
    :param string:
    :return:
    '''

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


# def solution(string, n):
# 用这种方法不好找最大的匹配位置
#     next_ = get_next(string + ' ')
#     start = -1
#     for i in range(2, n + 1):
#         if next_[i] >= 1:
#             start = i
#             if next_[i] - next_[i - 1] != 1:
#                 return 'false'
#     for i in range(next_[-1], 0, -next_[start]):
#         if (next_[i] / next_[start] - 1) & 1 == 0:
#             return string[:next_[i] // 2]


def solution(stirng, n):
    # 用双指针
    fpos, rpos, leng = 0, 1, 1
    while rpos < n:
        if string[fpos] == string[rpos]:
            fpos += 1
            rpos += 1
            if fpos == leng:
                fpos = 0
        else:
            leng = rpos + 1
            rpos += 1

    if leng > n // 2:
        return 'false'

    # 这里就是找到最短的长度，然后不断加一次，看string长度是否是它的整数倍，最大小心到string的长度
    i = 2
    while n % (leng * i) == 0 and (leng * i) != n:
        i += 1
    return string[:leng * (i - 1)]


# def solution(string, n):
#     for i in range(n // 2 + 1, 0, -1):
#         if len(string.replace(string[:i], '')) == 0:
#             return string[:i]
#     return 'false'


if __name__ == '__main__':
    string = input().strip()
    # string = 'abcabcabc'
    # string = 'aaaaaa'
    # string = ''
    ans = solution(string, string.__len__())
    print(ans)
