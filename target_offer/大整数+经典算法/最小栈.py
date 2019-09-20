# # 运行超时:您的程序未能在规定时间内运行结束，请检查是否循环有错或算法复杂度过大。
# # case通过率为66.67%
#
# # 去掉main函数 +  比较直接用string + 去掉strip函数 + 不用ifelse简写
# # 没用！
# 经检验是牛客网的错误，以前可以通过的代码现在都不可以通过了！
class Stack():
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def get_min(self):
        return self.min_stack[-1]

    def push(self, a):
        self.stack.append(a)
        self.min_stack.append(a if self.min_stack.__len__() == 0 or a <= self.min_stack[-1] else self.min_stack[-1])

    def pop(self):
        self.min_stack.pop()
        return self.stack.pop()


st = Stack()
Q = int(input())
for i in range(Q):
    # lst = input().split()
    # op = int(lst[0])
    op = input()
    if op == '0':
        print(st.get_min())
    elif op == '2':
        print(st.pop())
    else:
        st.push(int(op[2:]))
