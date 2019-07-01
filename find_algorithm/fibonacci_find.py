def create_fa():
    res = [1, 1]
    for i in range(2, 20):
        res.append(res[i - 1] + res[i - 2])
    return res


def fibonacc_find(arr, n, val):
    F = create_fa()

    low, high = 0, n - 1
    k = 0
    while high > F[k] - 1:
        k += 1

    arr = arr + [arr[-1]] * (F[k] - 1 - n)

    while low < high:
        mid = low + F[k - 1] - 1
        # 这里有两种情况， 1：可能是补全的值 2：可能是正常值， 用位置n-1做个判断
        if arr[mid] == val:
            if mid < n:
                return mid
            else:
                return n - 1
        elif arr[mid] < val:
            low = mid
            k -= 2
        else:
            high = mid - 1
            k -= 1
    return -1


import numpy as np

if __name__ == '__main__':
    data = np.random.rand(10)
    data = sorted(data)
    inx = fibonacc_find(data, len(data), data[7])
    print(inx)
