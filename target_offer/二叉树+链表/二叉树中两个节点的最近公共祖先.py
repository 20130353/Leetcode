class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


#
# # 存在的问题：
# # 没有考虑a或者b是none的情况
# # 运行超时:您的程序未能在规定时间内运行结束，请检查是否循环有错或算法复杂度过大。
# # case通过率为75.00%
# # 存在的问题：还有边角没有考虑清楚！
# # 解决方法：加入val == 0的情况。
# # 运行超时:您的程序未能在规定时间内运行结束，请检查是否循环有错或算法复杂度过大。
# # case通过率为80.00%
# # 解决方法：加入判断节点是否等于None和val==0的情况！ 这里需要单独判断！
# # 运行超时:您的程序未能在规定时间内运行结束，请检查是否循环有错或算法复杂度过大。
# # case通过率为95.00%
# # 还差在哪里？
# # 运行超时:您的程序未能在规定时间内运行结束，请检查是否循环有错或算法复杂度过大。
# # case通过率为80.00% --》 说明有重复的节点值

# # 用矩阵，不用dict来存放节点，需要排序！ -- 时间非常快！
# # AC！
#
# def solution(T, a, b):
#     '''
#         返回的最小公共祖先
#         如果两边都找到了，说明两个节点分别在当前的左右两边，那么当前节点就是最小公共祖先
#         如果左边找到了，那么左边就是最小的公共祖先
#         如果右边找到了，那么右边就是最小公共祖先
#     '''
#     if not T or not a or not b or T.val == 0:
#         return None
#
#     if T == a or T == b:
#         return T
#
#     left_father = solution(T.left, a, b)
#     right_father = solution(T.right, a, b)
#
#     if left_father and left_father.val != 0 and right_father and right_father.val != 0:
#         return T
#     if left_father and left_father.val != 0:
#         return left_father
#     if right_father and right_father.val != 0:
#         return right_father
#
#
# if __name__ == '__main__':
#     n, root = map(int, input().strip().split())
#     dict = {}
#     for i in range(n):
#         father, left, right = map(int, input().strip().split())
#         if father not in dict.keys():
#             dict[father] = Node(father)
#         if left not in dict.keys():
#             dict[left] = Node(left)
#         if right not in dict.keys():
#             dict[right] = Node(right)
#         dict[father].left = dict[left]
#         dict[father].right = dict[right]
#     a, b = map(int, input().strip().split())
#     ans = solution(dict[root], dict[a], dict[b])
#     print(ans.val) if ans else print('none')

# def solution(tree, n, root, a, b):
#     if root == 0 or root == a or root == b:
#         return root
#     left = tree[root - 1][1]
#     right = tree[root - 1][2]
#     left_father = solution(tree, n, left, a, b)
#     right_father = solution(tree, n, right, a, b)
#     if left_father != 0 and right_father != 0:
#         return root
#     elif left_father != 0:
#         return left_father
#     else:
#         return right_father
#
#
# if __name__ == '__main__':
#     n, root = map(int, input().strip().split())
#     tree = []
#     for i in range(n):
#         data = list(map(int, input().strip().split()))
#         tree.append(data)
#     a, b = map(int, input().strip().split())
#     tree.sort(key=lambda x: x[0])
#     ans = solution(tree, n, root, a, b)
#     print(ans)
