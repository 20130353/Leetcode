def solution(opt, n, string, target):
    if opt == 2:
        ans = 0
        for i in range(target.__len__()):
            pos = string.index(target[i])
            ans += (pos + 1) * pow(n, target.__len__() - i - 1)
        return ans
    else:
        target = int(target)
        bit = 1
        while pow(n, bit) < target:
            bit += 1
        ans = ''
        for i in range(bit, -1, -1):
            for j in range(n, 0, -1):
                # 这里一定要保证每个位置都有，所以验证条件target-(每个位置都为1的大小)
                sum_i = sum([pow(n, k) for k in range(i)])
                if j * pow(n, i) <= target - sum_i:
                    target -= j * pow(n, i)
                    ans += string[j - 1]
                    break
        return ans


if __name__ == '__main__':
    opt, n = map(int, input().strip().split(' '))
    string = input().strip()
    target = input().strip()
    ans = solution(opt, n, string, target)
    print(ans)
