# 运行超时:您的程序未能在规定时间内运行结束，请检查是否循环有错或算法复杂度过大。
# case通过率为70.00%
# 存在的问题：时间复杂度过大！

# 改进的点：标记不相等的个数，当新进入到下一个字符的时候，
# 判断出的字符是否相等，如果相等，忽略，如果不相等，不相等个数减1，
# 判断新加入的字符是否相等，如果相等，忽略，如果不相等，不相等个数加一
# 这种方法错误！ 因为这计算的总共不相等，但是不是对应位置不相等的个数！

# def solution(source, target, n, m):
#     ans = 0
#     for i in range(m, n + 1):
#         temp_source = source[i - m:i]
#         # print(temp_source)
#         for j in range(m):
#             if temp_source[j] != target[j]:
#                 ans += 1
#     return ans
#

###两个循环会超时
# 这里题目要求只能有两种字符，所以可以用a和b的数量直接算！
###扫描思想：例如s=aaabb，t=bab
###1.先看t中的第一个字符b在s中扫过s=[0:3]=aaa 所以有三次不同
###2.再看t中的第二个字符a在s中扫过s=[1:4]=aab 所以有一次不同
###3.再看t中的第三个字符b在s中扫过s=[2:5]=abb 所以有一次不同
###所以总共有五次不同
def solution(s, t, n, m):
    a = [0]
    for i in range(n):
        if s[i] == 'a':
            a.append(a[-1] + 1)
        else:
            a.append(a[-1])
    res = 0
    delta = n - m + 1
    for j in range(m):
        if t[j] == 'a':
            # j + delta 表示总的字符个数
            # j + delta - a[j + delta] 表示总字符个数-a的个数=b的个数
            res += j + delta - a[j + delta] - (j - a[j])
        else:
            res += a[j + delta] - a[j]
    return res


if __name__ == '__main__':
    string = input().strip()
    target = input().strip()
    ans = solution(string, target, string.__len__(), target.__len__())
    print(ans)
