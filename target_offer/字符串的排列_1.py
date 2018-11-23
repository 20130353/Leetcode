# -*- coding: utf-8 -*-
# author: sunmengxin
# time: 18-11-22
# file: 字符串的排列_1
# description:

# -*- coding:utf-8 -*-


# 反思：
#  1. 字符串就当做list来处理
#  2. 针对字符串去重使用可以使用set,sort和{}.fromkeys.keys(), 还可以数组遍历判断是否已经在数组中（in 和 not in 判断）

class Solution:

    def DFS(self, index, vis, res, total, ss, final_res):

        if index == total:
            final_res.append(res)

        for inx, each in enumerate(ss):
            if vis[inx] == False:
                vis[inx] = True
                res = ''.join([res,ss[inx]])
                self.DFS(index + 1, vis, res, total, ss, final_res)
                vis[inx] = False
                res = res[:-1]

    def Permutation(self, ss):
        if not ss or ss == '' or ss == "":
            return []

        vis = [False for _ in range(len(ss))]
        final_res = []
        self.DFS(0, vis, '', len(ss), ss, final_res)
        # return final_res
        # return {}.fromkeys(final_res).keys()
        # unique_res = []
        # temp = [unique_res.append(each) for each in final_res if not each in unique_res ]

        return sorted(list(set(final_res)))


if __name__ == '__main__':
    so = Solution()

    # so.Permutation('')
    print(so.Permutation("aab"))
    # so.Permutation(['a','b','c'])
