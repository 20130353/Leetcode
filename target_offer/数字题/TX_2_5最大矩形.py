if __name__ == '__main__':
    n = int(input().strip())
    ans = []
    max_ans = 0
    points = []
    for _ in range(n):
        pos = list(map(int, input().strip().split(' ')))
        points.append(pos)
        ans = abs(pos[0] - pos[2]) * abs(pos[1] - pos[3])
        print(ans)
        max_ans = max(max_ans, ans)
    print(max_ans + 2)

# 5
# 1 1 3 3 1
# 3 1 5 3 1
# 1 4 3 6 1
# 3 4 5 6 1
# 0 3 6 4 2
