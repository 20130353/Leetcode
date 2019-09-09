import sys


class Stack():
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def get_min(self):
        if self.min_stack:
            return self.min_stack[-1]
        else:
            print('wrong operation')
            return float('inf')

    def push(self, a):
        self.stack.append(a)
        if self.min_stack:
            self.min_stack.append(a if a <= self.min_stack[-1] else self.min_stack[-1])
        else:
            self.min_stack.append(a)

    def pop(self):
        if self.min_stack and self.stack:
            self.min_stack.pop()
            return self.stack.pop()
        else:
            print('wrong operation')
            return float('int')


if __name__ == '__main__':
    stack = Stack()
    n = int(input().strip())
    for _ in range(n):
        chars = list(map(int, input().strip().split(' ')))
        if chars[0] == 0:
            print(stack.get_min())
        elif chars[0] == 1:
            stack.push(int(chars[1]))
        elif chars[0] == 2:
            print(stack.pop())
        else:
            print('wrong operation')
            break
