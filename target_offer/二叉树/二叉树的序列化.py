# -*- coding:utf-8 -*-

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def Serialize(self, T):
        if not T:
            return '#'
        res = str(T.val)
        res += ',' + self.Serialize(T.left)
        res += ',' + self.Serialize(T.right)
        return res

    def deserialize(self, string):
        if not string:
            return None

        # 存在的问题：之前的写的代码是if string[0]=='#',返回None；存在一个误区：这里没有弹出#，会影响下一次的序列化！
        top = string.pop(0)
        if top == '#':
            return None
        else:
            T = TreeNode(int(top))
            T.left = self.deserialize(string)
            T.right = self.deserialize(string)
        return T

    def Deserialize(self, s):
        arr = s.replace('{', '').replace('}', '').split(',')
        # print(arr)
        return self.deserialize(arr)

    def level_vis(self, T):
        ans = []
        queue = [T]
        while queue.__len__() != 0:
            top = queue.pop(0)
            ans.append(top.val)
            if top.left:
                queue.append(top.left)
            if top.right:
                queue.append(top.right)
        return ans


if __name__ == '__main__':
    so = Solution()
    T = so.Deserialize('{8,6,10,5,7,9,11}')
    ans = so.level_vis(T)
    print('ans {}'.format(ans))
    string = so.Serialize(T)
    print('string {}'.format(string))
