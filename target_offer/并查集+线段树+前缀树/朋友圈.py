class Solution:
    def find_root(self, i, dict):
        while dict[str(i)] != i:
            dict[str(i)] = dict[str(dict[str(i)])] # 这里遇到不是一个根节点的时候要及时更改根节点
            i = dict[str(i)]
        return i

    def findCircleNum(self, M):
        if len(M) == 1:
            return len(M)
        n = len(M)
        dict = {}
        for i in range(n):
            dict[str(i)] = i

        res = n
        for i in range(n):
            for j in range(i+1, n):
                if M[i][j] == 1:
                    ri = self.find_root(i, dict)
                    rj = self.find_root(j, dict)
                    if ri != rj:
                        dict[str(i)] = rj
                        res -= 1
        return max(res, 1)


list = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]

ans = Solution().findCircleNum(list)
print(ans)
