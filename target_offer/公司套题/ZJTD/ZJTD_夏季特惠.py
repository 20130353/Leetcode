def solution(arr, n):
    def dfs(arr, n, vis, cur_index, ans):
        if cur_index >= n:
            total_cost = 0
            total_happy = 0
            total_youhui = 0
            for i in range(n):
                if vis[i] == 1:
                    total_cost += arr[1]
                    total_youhui += arr[0] - arr[1]
                    total_happy += arr[2]
            if total_youhui > (total_cost - 100):
                ans[0] = max(ans[0], total_happy)
            return

        vis[cur_index] = 1
        dfs(arr, n, vis, cur_index + 1, ans)
        vis[cur_index] = 0

    ans = [0]
    vis = [0] * n
    dfs(arr, n, vis, -1, ans)
    return ans[0]


if __name__ == '__main__':
    n = int(input().strip())
    arr = []
    for _ in range(n):
        a, b, c = map(int, input().strip().split(' '))
        arr.append((a, b, c))
    ans = solution(arr, n)
    print('%d' % ans)
