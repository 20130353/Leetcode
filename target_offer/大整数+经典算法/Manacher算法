def manacher(arr):
    print(arr)
    if not arr or len(arr) <= 0:
        return 0
    parr = [0 for _ in range(len(arr))]
    R = 0
    C = 0
    max_len = 0
    for i in range(len(arr)):
        parr[i] = min(parr[2 * C - 1], R - i) if i < R else 1

        while i - parr[i] >= 0 and i + parr[i] < len(arr) and arr[i - parr[i]] == arr[i + parr[i]]:
            parr[i] += 1

        if i + parr[i] - 1 > R:
            R = i + parr[i] - 1
            C = i
        max_len = max(max_len, parr[i])

    return max_len - 1

# 求解最长回文子串
if __name__ == '__main__':
    arr = 'ababa'
    ans = manacher('#' + '#'.join(arr) + '#')
    print(ans)
