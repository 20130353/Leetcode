# 这道题和变形词的区别是旋转词只能变化一次，左变换后的部分依然是顺序的！
# 存在的问题：因为是拼接得到的，所以在此拼接可以得到原来的结果，所以只要判断s1是否在拼接后的字符串就可以了
# AC
def solution(s1, s2, n, m):
    if n != m or sorted(s1) != sorted(s2):
        return 'NO'

    for i in range(n):
        new_s2 = s2[i:] + s2[:i]
        if new_s2 == s1:
            return 'YES'

    return 'NO'


# 得到的收获：字符串判断是否包含，直接用in就可以了!
# 时间更短！
# AC
# def solution(s1, s2, n, m):
#     if n != m or sorted(s1) != sorted(s2):
#         return 'NO'
#
#     if s1 in s2 + s2:
#         return 'YES'
#
#     return 'NO'


if __name__ == '__main__':
    n, m = map(int, input().strip().split(' '))
    s1 = input().strip()
    s2 = input().strip()

    print(solution(s1, s2, n, m))
