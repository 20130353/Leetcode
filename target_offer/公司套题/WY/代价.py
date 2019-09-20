# AC
if __name__ == '__main__':
    arr = list(map(int, input().strip().split(' ')))
    arr.sort()
    ans = 0
    for i in range(1, arr.__len__()):
        ans += abs(arr[i] - arr[i - 1])
    print(ans)
