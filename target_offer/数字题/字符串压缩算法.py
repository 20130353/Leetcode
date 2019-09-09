def solution(string, n):
    if n == 1:
        return string

    ans = ''
    i = 0
    while i < n:
        j = i + 1
        while j < n and string[i] == string[j]:
            j += 1
        ans += str(j - i - 1) + string[i] if str(j - i) != '1' else string[i]
        i = j
    return ans


if __name__ == '__main__':
    string = input().strip()
    ans = solution(string, string.__len__())
    print(ans)
