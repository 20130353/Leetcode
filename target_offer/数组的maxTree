# 单调栈问题
# 一个数组的MaxTree定义：
# 数组必须没有重复元素
# MaxTree是一棵二叉树，数组的每一个值对应一个二叉树节点
# 包括MaxTree树在内且在其中的每一棵子树上，值最大的节点都是树的头
# 给定一个没有重复元素的数组arr，写出生成这个数组的MaxTree的函数，要求如果数组长度为N，则时间负责度为O(N)、额外空间负责度为O(N)。
# 有两种方法, 1. 大根堆 2. 单调栈, 这里我们用单调栈的方式实现

class Tree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# need one map to save the node
def find_max(arr):
    if not arr:
        return [], []
    stack = []
    left = []
    for each in arr:
        if len(stack) >= 1:
            while stack:
                top = stack[-1]
                if top < each:
                    stack.pop()
                    if stack:
                        left.append((top, stack[-1], each))
                    else:
                        left.append((top, None, each))
                else:
                    stack.append(each)
                    break
        if len(stack) < 1:
            stack.append(each)
    while stack:
        top = stack.pop()
        if stack:
            left.append((top, stack[-1], None))
        else:
            left.append((top, None, None))
    return left


def fill_child(map, father, child):
    if map.get(father):
        node = Tree(child)
        map[child] = node
        if map[father].left is None:
            map[father].left = node
        else:
            map[father].right = node
    else:
        map[father] = Tree(father)
        map[child] = Tree(child)
        map[father].left = map.get(child)


def pre_vis(head):
    if head:
        print(head.val)
        pre_vis(head.left)
        pre_vis(head.right)


def create_tree(arr):
    head = None
    map = {}
    max_arr = find_max(arr)
    for each in max_arr:
        if not each[1] and not each[2]:
            map[each[0]] = Tree(each[0])
            head = each[0]
        elif each[1] and not each[2]:
            fill_child(map, each[1], each[0])
        elif not each[1] and each[2]:
            fill_child(map, each[2], each[0])
        else:
            v = min(each[1], each[2])
            fill_child(map, v, each[0])
    return map[head]


if __name__ == '__main__':
    arr = [3, 5, 2, 4, 6, 0, 1, 5]
    # arr = [1]
    T = create_tree(arr)
    pre_vis(T)
