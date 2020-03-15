# 没想到全过了！
def solution(arr, n):
    if n <= 1:
        return n

    i, j = 0, 1
    max_leng = 1
    while j < n:
        k = j - 1
        while k >= i and arr[k] != arr[j]:
            k -= 1
        i = k + 1
        max_leng = max(max_leng, j - i + 1)
        # print('k {},i {},j {}, j - i + 1 {}'.format(k, i, j, j - i + 1))
        j += 1
    return max_leng


if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    ans = solution(arr, n)
    print(ans)
