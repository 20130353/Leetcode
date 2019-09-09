def solution(s1, s2, n, m):
    if n != m or sorted(s1) != sorted(s2):
        return 'YES'
    return 'NO'


if __name__ == '__main__':
    n, m = map(int, input().strip().split(' '))
    s1 = input().strip()
    s2 = input().strip()

    print(solution(s1, s2, n, m))
