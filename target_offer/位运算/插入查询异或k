
# 网易笔试题
# 有个初始集合：支持两种操作：1. 插入操作，2查询是否存在一个子集满足子集中所有的数字的异或值等于k。1表示插入，2表示查询k

def dfs(arr, k, cur_pos, flag, cur_ans):
    if flag[0]:
        return

    if cur_ans == k:
        flag[0] = True
        return

    if cur_pos >= len(arr):
        return

    dfs(arr, k, cur_pos + 1, flag, cur_ans ^ arr[cur_pos])
    dfs(arr, k, cur_pos + 1, flag, cur_ans)


if __name__ == '__main__':
    n = 9
    ops = [(1, 4),
           (2, 5),
           (1, 9),
           (1, 15),
           (2, 4),
           (1, 11),
           (2, 10),
           (2, 7),
           (2, 9)]
    arr = []
    for each in ops:
        if each[0] == 1:
            arr.append(each[1])
        else:
            flag = [False]
            ans = dfs(arr, each[1], 0, flag, 0)
            if flag[0]:
                print('YES')
            else:
                print('NO')
