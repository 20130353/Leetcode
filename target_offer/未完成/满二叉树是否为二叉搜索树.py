# 关键点是通过二叉树的前序遍历和中序便利得到整个二叉树的结构, 然后一次计算二叉树的左右节点

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.is_print = True


class Solution:

    def build_T(self, arr):
        if not arr:
            return None

        T = TreeNode(arr.pop(0))
        queue = [T]
        while arr:
            if queue:
                top = queue.pop(0)
                if arr:
                    top.left = TreeNode(arr.pop(0))
                    queue.append(top.left)
                if arr:
                    top.right = TreeNode(arr.pop(0))
                    queue.append(top.right)
        return T

    def in_vis(self, T):
        if not T:
            return
        res = []
        stack = []
        node = T
        pre_val = None
        while node or stack:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                if not pre_val:
                    pre_val = node.val
                else:
                    cur_val = node.val
                    if cur_val < pre_val:
                        return False
                    else:
                        pre_val = cur_val
                node = node.right
        return True


if __name__ == '__main__':
    import sys

    for line in sys.stdin:
        if len(line) <= 0:
            print('')
        else:
            arr = list(map(int, line.strip().split(',')))
            solu = Solution()
            T = solu.build_T(arr)
            ans = solu.in_vis(T)
            print(ans)