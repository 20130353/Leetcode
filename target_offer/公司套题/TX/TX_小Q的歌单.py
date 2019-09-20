# 存在的问题是：每首歌表示是不一样的！
# 答案错误:您提交的程序没有通过所有的测试用例
# case通过率为40.00%

# 存在的问题：对于sum和都不可能为k的直接等于0
# 答案错误:您提交的程序没有通过所有的测试用例
# case通过率为50.00%

# AC

def solution(arr, n, w):
    # 长度，数量
    if sum(arr) < w:
        return 0
    if sum(arr) == w:
        return 1

    # print('arr {},w {}'.format(arr, w))
    dp = [0] * (w + 1)
    dp[0] = 1

    for i in range(1, n + 1):
        # print('i {},dp {}'.format(i, dp))
        for j in range(w, arr[i - 1] - 1, -1):
            dp[j] += (dp[j - arr[i - 1]])
    # print('final dp {}'.format(dp))
    return dp[w] % (1000000007)


if __name__ == '__main__':
    W = int(input().strip())
    leng1, num1, leng2, num2 = map(int, input().strip().split(' '))
    ans = solution([leng1] * num1 + [leng2] * num2, num1 + num2, W)
    print(ans)
