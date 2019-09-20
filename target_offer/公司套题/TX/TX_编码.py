# 答案错误:您提交的程序没有通过所有的测试用例
# case通过率为33.33%
# 我的错误是在每一位的加只加了当前位，但是没有加后面变化过的位置
# 还有一个错误是：
# 我理解是a,aa,aaa,aaaa
# 实际是a,b,c...aa,ab,...aaa,aab...aaaa这样

# 比如
# befc
# b从最右边的第一位，右边的第二位，右边的第三位，右边的第四位，每一个位置上都有25中可变性。结果应该是2*(25^3+25^2+25^1)
# e从最右边的第一位，右边的第二位，右边的第三位，开始
# f从最右边的第一位，右边的第二位
# c从最右边的第一位

if __name__ == '__main__':
    string = input().strip()
    chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y']
    ans = 0
    temp_sum = []
    for i in range(4):
        if len(temp_sum) == 0:
            temp_sum.append(pow(25, i))
        else:
            temp_sum.append(pow(25, i) + temp_sum[-1])
    temp_sum.reverse()

    for i in range(0, string.__len__()):
        ans += chars.index(string[i]) * temp_sum[i] + 1
    print(ans - 1)
