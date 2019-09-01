# 连续子数组的异或最大和问题
# 这道题的关键是构建两个dp数组，min值的来源不一定是min*each,也有可能是max*each
# 但是遇到数据不能通过，不能通过的原因是数据量太大了。

# 用字典树解决
# 建立字典树
# 在字段树中查询相反数或者，如果没有相反的就查询相同的
class Node:
    def __init__(self):
        self.next = {0: None, 1: None}

# 这里计算的输入一个数，找到一个数使其异或值最大的
#如果要计算子数组的最大异或者，那么存入的时候就需要存入到ai的最大异或和
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


# def solution(arr, n):
#     if n <= 0:
#         return 0
#
#     min_dp = [0]
#     max_dp = [0]
#     max_value = -float('inf')
#     for inx, each in enumerate(arr):
#         v1 = each ^ min_dp[-1]
#         v2 = each ^ max_dp[-1]
#         temp_min = min(v1, v2, each)
#         temp_max = max(v1, v2, each)
#         min_dp.append(temp_min)
#         max_dp.append(temp_max)
#         max_value = max(max_value, max_dp[-1])
#     return max_value

if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]
    T = TrieTree()
    for i in range(len(arr)):
        T.insert(arr[i])
    print(T.query(10))