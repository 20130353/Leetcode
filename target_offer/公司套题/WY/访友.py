
# AC
if __name__ == '__main__':

    n = int(input().strip())
    ans = int(n / 5)
    if n % 5 != 0:
        ans += 1
    print(ans)
