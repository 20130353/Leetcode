# 单调栈问题
# 给定一个数组, 找到左边第一个比它小的数字,和 右边比它小的数字


def solution(arr):
    stack = []
    left, right = [], []
    for i in range(len(arr)):
        while len(stack) > 0 and stack[-1][0] > arr[i]:
            stack.pop()
        if stack.__len__() > 0:
            left.append(stack[-1][1])
        else:
            left.append(-1)
        stack.append((arr[i], i))

    stack = []
    for i in range(len(arr) - 1, -1, -1):
        while len(stack) > 0 and stack[-1][0] > arr[i]:
            stack.pop()
        if stack.__len__() > 0:
            right.append(stack[-1][1])
        else:
            right.append(-1)
        stack.append((arr[i], i))
    return left, right[::-1]


if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    left, right = solution(arr)
    for a, b in zip(left, right):
        print('{} {}'.format(a, b))
