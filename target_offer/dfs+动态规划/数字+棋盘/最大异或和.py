
# 没有找到正确答案，不知道为为什么？

class Node:
    def __init__(self):
        self.next = {0: None, 1: None}

class TrieTree:
    def __init__(self):
        self.head = Node()

    def insert(self, key):
        # 核心思想就是提取每一位数字，判断数字是否存在，沿着路径一直构造
        cur = self.head
        for i in range(31, -1, -1):
            path = (key >> i) & 1  # 每一位
            if cur.next.get(path) is None:  # 如果没有就插入
                cur.next[path] = Node()
            cur = cur.next[path]

    def query(self, key):
        # 核心思想就是提取每一位数字判断是否存在相异的数字，如果存在就用，如果不存在就不用
        cur = self.head
        res = 0
        for i in range(31, -1, -1):
            path = (key >> i) & 1  # 提取每一位的数字（0，1）
            best = path if i == 31 else path ^ 1  # 期望的数字就是和原来的数字相异的数字
            best = best if cur.next.get(best) else best ^ 1  # 实际要选的路
            res |= (path ^ best) << i  # 设置答案的每一位，将得到的值移动到对应的位数
            cur = cur.next.get(best)  # 继续沿着best的路径走下去
        return res


if __name__ == '__main__':
    arr = [3, -28, -29, 2]
    T = TrieTree()
    sum = 0
    max_value = -float('inf')
    for i in range(len(arr)):
        sum ^= arr[i]
        T.insert(sum)
        max_value = max(max_value, T.query(sum) ^ sum)  # 这里是为什么呢？？？
        print('sum is ', sum)
    print(max_value)
