# 给定一个数组序列, 需要求选出一个区间, 使得该区间是所有区间中经过如下计算的值最大的一个：
# 区间中的最小数 * 区间所有数的和最后程序输出经过计算后的最大值即可，不需要输出具体的区间。如给定序列  [6 2 1]则根据上述公式, 可得到所有可以选定各个区间的计算值:

# 以后做题还是直接模拟比较好！
# 运行超时:您的程序未能在规定时间内运行结束，请检查是否循环有错或算法复杂度过大。
# case通过率为30.00%

# if __name__ == '__main__':
#     n = int(input().strip())
#     arr = list(map(int, input().strip().split(' ')))
#     max_value = -float('inf')
#     i, j = 0, 0
#     sum_i = 0
#     while j < n:
#         sum_i += arr[j]
#         if j != 0 and arr[j] >= arr[j - 1]:
#             max_value = max(arr[j - 1] * sum_i, max_value)
#             max_value = max(arr[j] ** 2, max_value)
#             i = j
#             sum_i = arr[j]
#             j += 1
#         else:
#             max_value = max(sum_i * arr[j], max_value)
#             j += 1
#     print(max_value)


# 运行超时:您的程序未能在规定时间内运行结束，请检查是否循环有错或算法复杂度过大。
# case通过率为60.00%
# 提高了30%

# 这个可以写成左边第一个比他小的数字，和右边第一个比他小的是数字的下标，然后直接取用
# 窗口：维护一个递增的序列，每次把窗口内比自己大的数字都清除掉！
# 运行超时:您的程序未能在规定时间内运行结束，请检查是否循环有错或算法复杂度过大。
# case通过率为80.00%
# def solution(arr, n):
#     lwindow = [0]
#     left_min = [0]
#     for i in range(1, n):
#         while lwindow.__len__() > 0 and arr[i] <= arr[lwindow[-1]]:
#             lwindow.pop()
#         left_min.append(lwindow[-1] + 1) if lwindow.__len__() > 0 else left_min.append(0)
#         lwindow.append(i)
#
#     rwindow = [n - 1]
#     right_min = [n] * n
#     for i in range(n - 1, -1, -1):
#         while rwindow.__len__() > 0 and arr[i] <= arr[rwindow[-1]]:
#             rwindow.pop()
#         right_min[i] = rwindow[-1] if rwindow.__len__() > 0 else n
#         rwindow.append(i)
#
#     # print('left {}'.format(left_min))
#     # print('right {}'.format(right_min))
#     ans = -float('inf')
#     for i in range(n):
#         # print('i {}, ans {}'.format(i, sum(arr[left_min[i]:right_min[i]]) * arr[i]))
#         ans = max(ans, sum(arr[left_min[i]:right_min[i]]) * arr[i])
#
#     return ans


# AC
def solution(arr, n):
    p = [arr[0]]
    for i in range(1, n):  # 预处理累计求和
        p.append(p[i - 1] + arr[i])
    ans = 0
    stack = [0]
    for i in range(1, n):
        # 比当前这个元素小的留下，大的弹出
        while stack and arr[stack[-1]] >= arr[i]:  # 栈非空且栈顶元素大于当前元素，为了维持单调递增栈，弹出栈顶元素
            min_num = arr[stack.pop()]  # 栈顶元素为区间最小值，出栈。左边界为栈顶或者第一个元素，有边界是当前元素
            # 为什么右边界可以不在一次过程中直接找到，而是靠遍历的方式就可以
            # 这里会错过一段，但是怎么保证错过的这一段一定不是正确解！
            ans = max(ans, (p[i - 1] - (p[stack[-1]] if len(stack) > 0 else 0)) * min_num)
        stack.append(i)
    print(ans)

if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    ans = solution(arr, n)
    print(ans)