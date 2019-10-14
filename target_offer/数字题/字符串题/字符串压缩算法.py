# 输入一串字符，请编写一个字符串压缩程序，将字符串中连续出现的重复字母进行压缩，并输出压缩后的字符串。
# 例如：
# aac 压缩为 1ac
# xxxxyyyyyyzbbb 压缩为 3x5yz2b


def solution(string, n):
    ans = ''
    i = 0
    while i < n:
        j = i + 1
        while j < n and string[i] == string[j]:
            j += 1
        ans += str(j - i - 1) + string[i] if j - i != 1 else string[i]
        i = j
    return ans


if __name__ == '__main__':
    string = input().strip()
    ans = solution(string, string.__len__())
    print(ans)
