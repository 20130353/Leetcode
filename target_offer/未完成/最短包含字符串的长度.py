# 运行超时:您的程序未能在规定时间内运行结束，请检查是否循环有错或算法复杂度过大。
# case通过率为28.57%
# 加入长度判断 --》 无用！
# 有个疑问：包含所有字符是顺序包含吗？


def solution(source, target, n, m):
    if target in source:
        return target.__len__()

    if target.__len__() >= source.__len__():
        return 0

    for each in target:
        if each not in string:
            return 0

    min_dis = float('inf')
    for i in range(n):
        if source[i] == target[0]:
            k, j = i + 1, 1
            while j < m and k < n:
                if source[k] == target[j]:
                    j += 1
                    k += 1
                else:
                    k += 1
            if j == m:
                min_dis = min(min_dis, k - i)
    return min_dis if min_dis != float('inf') else 0


if __name__ == '__main__':
    string = input().strip()
    target = input().strip()
    ans = solution(string, target, string.__len__(), target.__len__())
    print(ans)

# 423141234578909
# 1239
