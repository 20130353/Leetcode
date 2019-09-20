# 感觉会超时！
# 运行超时:您的程序未能在规定时间内运行结束，请检查是否循环有错或算法复杂度过大。
# case通过率为20.00%

# 改成上界为n/10
# 运行超时:您的程序未能在规定时间内运行结束，请检查是否循环有错或算法复杂度过大。
# case通过率为20.00%

# 我原先不知道o(n^2)改时间复杂度怎么改，想过二分查找，但是不知道二分查找的停止条件是什么？
# 看了解析才知道停止条件是右边界-左边界=1
# 又看了解析，发现其实按照我原先的想法，遍历所有也是可以节省时间的。

def cal(get, n):
    total = 0
    leave = n
    flag = 0
    while leave > 0:
        flag += 1
        if flag & 1 == 1:
            total += min(leave, get)
            leave -= min(leave, get)
        else:
            leave -= leave // 10
    return total


#
# def solution(n):
#     if n == 1:
#         return 1
#
#     get = float('inf')
#     total_get = float('inf')
#     for i in range(1, n // 10):
#         total = cal(i, n)
#         if total >= n / 2 and (total - n / 2) < (total_get - n / 2):
#             get = i
#             total_get = total
#     return get


# 答案错误:您提交的程序没有通过所有的测试用例
# case通过率为90.00%
# 44797688750076026
# 对应输出应该为:
# 1758731482835768
# 你的输出为:
# 1758731482835767
# 这个错误就是我的边界没有对！
#

def solution(n):
    left, right = 1, max(n // 10, 1)
    min_mid, min_val = None, float('inf')
    while left <= right:
        mid = left + (right - left) // 2
        total = cal(mid, n)
        if total >= (n + 1) // 2:
            if total < min_val:
                min_val = total
                min_mid = mid
            right = mid - 1
        else:
            left = mid + 1
    return min_mid


if __name__ == '__main__':
    n = int(input().strip())
    ans = solution(n)
    print(ans)
