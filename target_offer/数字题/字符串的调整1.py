# # 存在的问题：
# # 新开了数组 --> 应该在原来的数组中移动就好
# def solution(string, n):
#     new_arr = ''
#     num = 0
#     for i in range(n):
#         if string[i] != '*':
#             new_arr += string[i]
#         else:
#             num += 1
#
#     return '*' * num + new_arr

# 存在的问题：
# 新开了数组 --> 应该在原来的数组中移动就好

# 存在的问题：在原地并没有使内存和时间减小
def solution(string, n):
    num = 0
    for i in range(n):
        if string[i] != '*':
            string[i - num] = string[i]
        else:
            num += 1
    return ''.join(['*'] * num + string[:n - num])


if __name__ == '__main__':
    string = input().strip()
    ans = solution(list(string), string.__len__())
    print(ans)
