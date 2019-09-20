# 存在的问题：
# 1. 如果是中间存在最长的间隔字符串呢？ 将所有的连续结果保存下来，找最大的！
#
# def solution(string):
#     new_string = ''
#     for i in range(1, string.__len__()):
#         if string[i] == string[i - 1]:
#             new_string = string[:i][::-1] + string[i:][::-1]
#             j = 1
#             while j < new_string.__len__() and new_string[j] != new_string[j - 1]:
#                 j += 1
#             return j
#     return string.__len__()


# 试一下暴力的方法
# 运行超时:您的程序未能在规定时间内运行结束，请检查是否循环有错或算法复杂度过大。
# case通过率为20.00%

# 中间相同，两边相反可以凑多一个间隔
# 加了两边不相等就删除的判断
# 运行超时:您的程序未能在规定时间内运行结束，请检查是否循环有错或算法复杂度过大。
# case通过率为50.00%

# 原先是从每个位置断开！
# 从间隔的地方断开翻转
# 运行超时:您的程序未能在规定时间内运行结束，请检查是否循环有错或算法复杂度过大。
# case通过率为50.00%
def cal_leng(string):
    ans = []
    pos = []
    i, j = 0, 1
    while i < string.__len__():
        while j < string.__len__() and string[j] != string[j - 1]:
            j += 1
        ans.append(j - i)
        pos.append(j)
        i = j
        j = i + 1
    return ans, pos


# def solution(string, smap, max_leng):
#     leng, pos = cal_leng(string)
#     max_leng[0] = max(max_leng[0], max(leng))
#     if max_leng[0] == string.__len__():
#         return
#
#     if string[0] == string[-1]:
#         return
#
#     # print('leng {},pos {}'.format(leng, pos))
#     for i in pos:
#         # print('string {},i {},string[:i] {},string[i:] {}'.format(string, i, string[:i], string[i:]))
#         new_string = string[:i][::-1] + string[i:][::-1]
#         if new_string not in smap:
#             smap.append(new_string)
#             solution(new_string, smap, max_leng)

# 存在错误：可能本身就存在连续的间隔
# 两端没有相反的，就返回找一圈之后的最大值
# 您的代码已保存
# 答案正确:恭喜！您提交的程序通过了所有的测试用例
# 这里编程有个问题，因为是从不连续的地方断开，那么断开之后两端就是一样的了，那么下一次一定不可以拼接，所以写成while会浪费时间
def solution(string):
    if string.__len__() <= 1:
        return string.__len__()
    i = 1
    while True:
        while i < string.__len__() and string[i] != string[i - 1]:
            i += 1
        if i < string.__len__() and string[0] != string[-1]:
            string = string[:i][::-1] + string[i:][::-1]
        else:
            leng, pos = cal_leng(string)
            return max(leng)


# 别人的最优解！
# 字符串翻转，可以将其理解为环形结构，相对位置不变

# 我觉得不需要考虑成环形结构，
# 1. 考虑首尾不同能增加新的间隔的情况。
# 2. 考虑最大间隔是字符串的某个子串
# 所以考虑问题的形式应该是：本身字符串可以得到的解，和什么情况下能增大解长度
def solution(s):
    ans = 0
    pre = 0
    post = s.__len__() - 1
    # 这里比较好的计算从后面开始的连续间隔串
    if s[0] != s[-1]:
        while (s[pre] != s[pre + 1]):
            pre += 1
        while (s[post] != s[post - 1]):
            post -= 1
        ans = s.__len__() - post + pre + 1
    tmp = 1
    for i in range(s.__len__() - 1):
        if s[i] != s[i + 1]:
            tmp += 1
        else:
            ans = max(ans, tmp)
            tmp = 1
    ans = max(ans, tmp)
    return ans


if __name__ == '__main__':
    string = input().strip()
    ans = solution(string)
    print(ans)
