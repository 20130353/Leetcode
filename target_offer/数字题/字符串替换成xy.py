# @File  : 字符串替换成xy.py
# @Author: smx
# @Date  : 2019/8/18
# @Desc  :

# 存在的问题：字符串是否需要加后面的部分，不要分开来写，直接用string加的形式
#  存在的问题：内存超 -》 用map保存已经遍历过的字符串
#  请检查是否存在语法错误或者数组越界非法访问等情况 -》 应该是使用了python的限定字符 --》 还不是.
# 从网上找到解析：
#
# 1、数组确实越界了，注意数组的索引 --》 确定没有
#
# 2、如果递归爆栈，也会报这个错误。内存过大。本地不报错，因为我们本地内存很大，牛客上每个题都会有内存限制。 --》 感觉会是这个错误！
#
# 3、有可能是特殊案例，没有考虑周全，例如为空等

# 存在的问题：如果数据非常大，暴力需要转换成dp或者思考数据之间的关系


# def solution(string, count, mdict):
#     global min_count
#
#     if 'xy' not in string:
#         min_count = min(min_count, count)
#         return count
#
#     if count >= min_count:
#         return float('inf')
#
#     n = len(string)
#     for i in range(len(string) - 1):
#         if string[i] == 'x' and string[i + 1] == 'y':
#             new_string = string[:i] + 'yyx'
#             if i + 2 < n:
#                 new_string += string[i + 2:]
#             if new_string in mdict:
#                 min_count = min(min_count, mdict[new_string] + count)
#             else:
#                 mdict[new_string] = solution(new_string, count + 1, mdict)
#             return mdict[new_string] + count
#
# 遍历字符串，每次遇到y时，统计y之前的x的数量为p，将x全部移到y之后需要的替换次数为：2^p-1
# 当x的数量多时，整数溢出，使用快速幂的模运算。
def solution(string):
    num = 0
    count = 0
    if string[0] == 'x':
        count = 1
    X = count
    for i in range(1, len(string)):
        if string[i] == 'x':
            count += 1
            X = ((2 * X) + 1) % (10 ** 9 + 7)
        else:
            num = (num + X) % (10 ** 9 + 7)
    return int(num % (10 ** 9 + 7))


if __name__ == '__main__':
    string = input().strip()
    min_count = float('inf')
    print(solution(string))
