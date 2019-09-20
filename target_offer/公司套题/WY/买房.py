# AC
if __name__ == '__main__':
    n = int(input().strip())
    for _ in range(n):
        n, k = map(int, input().strip().split(' '))
        ans = min(n - k, k - 1) if min(n - k, k - 1) >= 0 else 0
        print('0 {}'.format(ans))
