# -*- coding:utf-8 -*-


# 解法1：暴力法用树来做，如果两个节点在左子树中，那么递归左子树，如果两个节点在右子树，那么递归右子树，如果两个节点分别在左右子树中(一个节点是当前节点，一个节点在左右子树中)，那么当前节点就是公共祖先，时间复杂度
# 解法2：暴力法用字符串来做，找到两个节点的位置ij， 从最大的节点开始向上遍历父节点，每次都是ij位置中较大的一个向上，直到两个节点的位置一样（这个做法本质和遍历树是一样的，但是因为树不能从下向上遍历所以用数组的方式）
# 解法3：倍增法，开始向上跳2i个，之后每一次都是跳上一次的一半步数，到两个节点到同一个高度，从最大步数开始一起尝试跳，如果太大就改小步数，一直到找到同一个节点为止
# 解法4：RMQ算法，mark一下，之后再看


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


# 二叉搜索树
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while 1:
            if not root:
                return root
            # p,q均小于根节点，到左子树里寻找公共祖先
            if p.val < root.val and q.val < root.val:
                root = root.left

            # p,q均小于根节点，到左子树里寻找公共祖先
            elif p.val > root.val and q.val > root.val:
                root = root.right

            # p,q其一小于或等于根节点，另一大于或等于根节点，该根节点就是公共祖先
            else:
                return root


# 普通的二叉树
class Solution:
    def lowestCommonAncestor(self, root, A, B):
        if (root is None or root == A or root == B):
            return root  # 若root为空或者root为A或者root为B，说明找到了A和B其中一个
        left = self.lowestCommonAncestor(root.left, A, B)  # 可能性是之前的节点只包含A，或者只包含B，或者同时包含AB，返回的包含A和B的最小公共祖先
        right = self.lowestCommonAncestor(root.right, A, B)  # 可能性是之前的节点只包含A，或者只包含B，或者同时包含AB
        if (left is not None and right is not None):  # A和B在不同的子树上都找到了，那么同时包含的情况就不存在了。
            return root  # 若左子树找到了A，右子树找到了B，说明此时的root就是公共祖先
        if (left is None):  # 若左子树是none右子树不是，说明右子树找到了A和B（不存在不包含节点的情况），右边返回了AB的最小公共祖先
            return right
        if (right is None):  # 若右子树是none左子树不是，说明右子树找到了A和B（不存在不包含节点的情况），左边返回了AB的最小公共祖先
            return left
        return None


# 倍增法（基本是靠图来实现，所以这里我就简单写了个伪代码）
class Node:
    def __init__(self, val):
        self.next = []
        self.val = val


class Solution:
    # 遍历每一层的所有节点
    def dfs(self, now, depth, f):
        for i in range(len(now.next)):
            if now.next[i] not in depth.keys():
                depth[now.next[i]] = depth[now] + 1
                f[now.next[i]][0] = now
                self.dfs(now.next[i], depth, f)

    def pre(self, n):
        f = [[0] * 19 for _ in range(n)]
        for i in range(19):
            for j in range(n):
                f[j][i] = f[f[j][i - 1]][i - 1]
        return f

    def lca(self, x, y, depth, f):
        # x表示较深的节点，y表示较浅的节点
        if depth[x] < depth[y]:
            x, y = y, x

        # x一直跳到和y一样高的高度
        for i in range(19, -1, -1):
            if depth[f[x][i]] >= depth[y]:
                x = f[x][i]

        if x == y:
            return x

        # x和y一起跳
        for i in range(19, -1, -1):
            if f[x][i] != f[y][i]:
                x = f[x][i]
                y = f[y][i]
        return f[x][0]

    def lca_main(self, T, n, x, y):
        '''
        :param T: 根节点
        :param n: 最深的深度
        :param x: 要查找的节点
        :param y: 要查找的节点
        :return:
        '''

        depth = {T: 1}
        f = self.pre(n)
        self.dfs(T, depth, f)
        ans = self.lca(x, y, depth, f)
        return ans


if __name__ == '__main__':
    a = Tree = TreeNode(2)
    b = Tree.left = TreeNode(1)
    c = Tree.right = TreeNode(3)
    d = b.left = TreeNode(4)
    s = Solution()
    print(s.lowestCommonAncestor(a, b, c).val)
