# 出现的问题：
# 新的字符串的顺序和原来的顺序是一样的，如果是用位置调换的方式，得到的顺序是相反的
# def solution(string, n, size):
#     if size == 0:
#         return string[:-1:-1]
#
#     if size == n:
#         return string
#
#     for i in range(size):
#         string[i], string[n - i - 1] = string[n - i - 1], string[i]
#     return string

def solution(string, n, size):
    return ''.join(string[size:] + string[:size])


if __name__ == '__main__':
    size = int(input().strip())
    string = input().strip()
    ans = solution(list(string), string.__len__(), size)
    print(ans)
