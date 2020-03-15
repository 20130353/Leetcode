import sys
from collections import Counter


class Node:
    def __init__(self, val, weight=0):
        self.val = val
        self.weight = weight
        self.left = None
        self.right = None


# python的堆不支持结构体！
# 所以只能用list，sort排序自定义!

# 出现的问题：输入输出有问题！判断输入的string是否是空字符串
# 计算高度直接用层次遍历，注意从0开始，不是从1开始
# class Huffman:
#     def build(self, dict):
#         data = []
#         for ch in dict.keys():
#             heapq.heappush(data, Node(ch, dict[ch]))
#
#         while len(data) > 1:
#             n1 = heapq.heapop(data)
#             n2 = heapq.heapop(data)
#             new_node = Node('*', n1.weight + n2.weight, max(n1.height, n2.height))
#             new_node.left = n1
#             new_node.right = n2
#             heapq(data, new_node)
#         return data[0]
#
#     def get_encode_length(self, node, dict):
#         ans = 0
#         queue = [node]
#         while queue.__len__() > 0:
#             top = queue.pop(0)
#             if top.left:
#                 queue.append(top.left)
#             if top.right:
#                 queue.append(top.right)
#             if top.left is None and top.right is None:
#                 ans += top.height * dict[top.val]


class Huffman:
    def build(self, dict):
        data = [Node(ch, dict[ch]) for ch in dict.keys()]
        while len(data) > 1:
            data.sort(key=lambda x: x.weight)
            n1, n2 = data.pop(0), data.pop(0)
            new_node = Node('*', n1.weight + n2.weight)
            new_node.left = n1
            new_node.right = n2
            data.append(new_node)
        return data[0]

    def get_encode_length(self, node, dict):
        ans = 0
        queue = [node]
        height = 0
        while queue.__len__() > 0:
            size = len(queue)
            while size > 0:
                top = queue.pop(0)
                if top.left:
                    queue.append(top.left)
                if top.right:
                    queue.append(top.right)
                if top.left is None and top.right is None:
                    # print('-------------top.val {},top.weight {}, height {}'.format(top.val, top.weight, height))
                    ans += height * dict[top.val]
                size -= 1
            height += 1
        return ans


if __name__ == '__main__':
    try:
        while True:
            line = sys.stdin.readline().strip()
            if line == '':
                break
            counter = Counter(list(line))
            T = Huffman().build(counter)
            ans = Huffman().get_encode_length(T, counter)
            print(ans)
    except:
        pass
