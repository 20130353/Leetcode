# 和我自己的想法一样：
# 最小值
# 如果是完全相同，那么就是组合数
# 如果不重复，就是排序之后的相减的结果
# 如果重复，就是重复数字的组合数


# 最大值
# 最小值个数*最大值个数

# 这道题的关键是搞清楚是排列还是组合!

# 答案错误:您提交的程序没有通过所有的测试用例
# case通过率为90.00%
# 出现的问题：排序直接的最小值应该是a[i]-a[i+1],i不区分奇数或者偶数
# AC

from collections import Counter


def solution(arr, n):
    if set(arr).__len__() == 1:
        return n * (n - 1) / 2, n * (n - 1) / 2

    counter = Counter(arr)
    if counter.most_common(1)[0][1] >= 2:
        min_num = 0
        for each in counter.items():
            if each[1] >= 2:
                min_num += each[1] * (each[1] - 1) / 2
    else:
        arr.sort()
        min_value, min_num = float('inf'), -1
        for i in range(n - 1):
            if abs(arr[i] - arr[i + 1]) < min_value:
                min_value = abs(arr[i] - arr[i + 1])
                min_num = 1
            elif abs(arr[i] - arr[i + 1]) == min_value:
                min_num += 1

    return min_num, arr.count(min(arr)) * arr.count(max(arr))


if __name__ == '__main__':
    # n = 6
    # arr = [45, 12, 45, 32, 5, 6]
    # n = 6
    # arr = [1, 1, 1, 1, 1, 1]
    # n = 3
    # arr = [1, 2, 3]
    # n = 6
    # arr = [1, 2, 3, 4, 5, 6]

    try:
        while True:
            line = input().strip()
            if line == '':
                break
            else:
                n = int(line)
            arr = list(map(int, input().strip().split(' ')))
            ans = solution(arr, n)
            print('%d %d' % (ans[0], ans[1]))
    except:
        pass
