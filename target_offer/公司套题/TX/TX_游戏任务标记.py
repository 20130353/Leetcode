
# AC
n, m = map(int, input().strip().split(' '))
if n <= 0 or n > 1024 or m <= 0 or m > 1024:
    print(-1)
elif n == m:
    print(1)
else:
    print(0)
