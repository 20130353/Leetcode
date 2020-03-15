#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 简化路径.py
# @Author: smx
# @Date  : 2020/2/11
# @Desc  :

class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path = path.split("/")

        for item in path:
            if item == "..":
                if stack : stack.pop()
            elif item and item != ".":
                stack.append(item)
        return "/" + "/".join(stack)

# 我的代码存在的问题是没有使用/将字符串分割就直接判断，导致判断复杂！
# class Solution:
#     def simplifyPath(self, path):
#         if not path or path == '/' or path == '//':
#             return '/'
#
#         stack = []
#         i = 0
#         while i < len(path):
#             if path[i].isalnum() or path[i] in '_-':
#                 stack.append(path[i])
#             elif path[i] == '/':
#                 if not stack or stack[-1] != '/':
#                     stack.append(path[i])
#             elif path[i] == '.':
#                 if i + 2 < len(path) and path[i + 2] == '.' and path[i + 1] == '.':
#                     stack.append('...')
#                     i += 2
#                 elif i + 1 < len(path) and path[i + 1] == '.':
#                     if i + 2 < len(path) and path[i + 2].isalpha():
#                         stack.append(path[i:i + 2])
#                         i += 1
#                     else:
#                         if stack and stack[-1] == '/': stack.pop()
#                         while stack and stack[-1] != '/':
#                             stack.pop()
#                         if stack and stack[-1] == '/': stack.pop()
#                         i += 1
#                 else:
#                     if i + 1 < len(path) and path[i + 1].isalpha():
#                         stack.append(path[i])
#                     else:
#                         stack: stack.pop()
#             i += 1
#         if not stack:
#             return '/'
#         ans = ''.join(stack)
#         if ans[0] != '/': ans = '/' + ans
#         if len(ans) > 1 and ans[-1] == '/': ans = ans[:-1]
#         return ans


if __name__ == '__main__':
    string = "/home/foo/.ssh/../.ssh2/authorized_keys/"
    res = Solution().simplifyPath(string)
    print(res)
