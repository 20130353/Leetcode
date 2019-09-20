# 感觉会超时！
# 运行超时:您的程序未能在规定时间内运行结束，请检查是否循环有错或算法复杂度过大。
# case通过率为10.00%
# 寻找最小公倍数的时候每次都是乘max(arr)

# 运行超时:您的程序未能在规定时间内运行结束，请检查是否循环有错或算法复杂度过大。
# case通过率为10.00%
# 存在的问题：正确的case这么少，肯定是算法有问题！
# 直接使用find_minbei也已经超时了！
# 保证m是倍数-1，保证余数最大。
# 但是为什么sum(arr)就是最小公倍数呢？
# 这里有误解，sum(arr)-n不是最小公倍数，是最后余数的求和,每个余数都是x-1,所有的余数就是sum(arr)-n*1
#
# AC
# 收获：一般如果case只过了很少的话，就是想法不对！
# def find_minbei(arr):
#     c = max(arr)
#     while True:
#         i = 0
#         while i < arr.__len__() and c % arr[i] == 0:
#             i += 1
#         if i == arr.__len__():
#             return c
#         c *= max(arr)


if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    print(sum(arr) - n)
