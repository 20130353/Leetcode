# -*- coding:utf-8 -*-

# 只有一位不同！
# 从左变到右
# AC


# 我这道题没有发现对称性的规律！

# class GrayCode:
#     def right2left_dfs(self, cur, cur_pos, n, total_res):
#         if cur_pos < 0:
#             return
#
#         total_res.append(''.join(cur))
#         cur[cur_pos] = '1'
#         self.right2left_dfs(cur, cur_pos - 1, n, total_res)
#
#     def left2right_dfs(self, cur, cur_pos, n, total_res):
#         if cur_pos >= n:
#             return
#
#         # print('cur {}, cur_pos'.format(cur, cur_pos))
#         total_res.append(''.join(cur))
#         cur[cur_pos] = '0'
#         self.left2right_dfs(cur, cur_pos + 1, n, total_res)
#
#     def getGray(self, n):
#         total_res = []
#         self.right2left_dfs(['0'] * n, n - 1, n, total_res)
#         self.left2right_dfs(['1'] * n, 0, n, total_res)
#         return total_res


class GrayCode:

    def getGray(self, n):
        if n == 1:
            return ['0', '1']

        res = []
        v = self.getGray(n - 1)
        for i in range(v.__len__()):
            res.append('0' + v[i])

        for i in range(v.__len__() - 1, -1, -1):
            res.append('1' + v[i])
        return res


if __name__ == '__main__':
    # n = 1
    # n = 2
    # n = 3
    print(GrayCode().getGray(n))
