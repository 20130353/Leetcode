# 运行超时:您的程序未能在规定时间内运行结束，请检查是否循环有错或算法复杂度过大。
# case通过率为60.00%

def get_prime(max_number=1000000):
    prime_bool = [1] * max_number
    prime_bool[0] = prime_bool[1] = 0
    for i in range(2, int(max_number ** 0.5) + 1):
        if prime_bool[i] == 1:
            prime_bool[i * i:max_number:i] = [0] * len(prime_bool[i * i:max_number:i])

    prime_res_bool = []
    for i in range(max_number):
        if prime_bool[i]:
            prime_res_bool.append(i)
    return prime_res_bool


def divisor(n, prime_list):
    div = []
    for i in range(prime_list.__len__()):
        if prime_list[i] <= n and n % prime_list[i] == 0:
            div.append(prime_list[i])
        if prime_list[i] >= n:
            return div
    return div


#  改成找到第一组除数
# 答案错误:您提交的程序没有通过所有的测试用例
# case通过率为70.00%
# 可能是找最大质数小了


# 质数上限提到100000
# 请检查是否存在语法错误或者数组越界非法访问等情况
# case通过率为90.00%

# 质数上限是1000000
# 可以先把质数都保存下来，然后直接用！

# 思路：
# 找到第一组数的素数约数，之后的每一组数字都判断是否能被素数约数整数（任意一个能被整除都行），如果两个都不能被整除，就去掉这个素数约数，最后在所有剩下的素数约数中找最大的。
# 只过了90%，感觉没有办法在开大约数数组了。
if __name__ == '__main__':
    prime_list = get_prime()
    print(prime_list)

    n = int(input().strip())
    a, b = map(int, input().strip().split(' '))
    s = set(divisor(a, prime_list) + divisor(b, prime_list))
    for i in range(n - 1):
        a, b = map(int, input().strip().split(' '))
        s = [each for each in s if a % each == 0 or b % each == 0]
    print(max(s))
