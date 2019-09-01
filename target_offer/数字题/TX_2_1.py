import sys
from collections import Counter
number = int(sys.stdin.readline().strip())
ans = []
for i in range(number):
    length = int(sys.stdin.readline().strip())
    numbers = list(map(int, sys.stdin.readline().strip().split()))
    count = Counter(numbers)
    max_c = max(count.values())
    if max_c > length/2:
        ans.append('NO')
    else:
        ans.append('YES')

for i in ans:
    print(i)