# -*- coding: utf-8 -*-
# author: sunmengxin
# time: 18-11-15
# file: 从尾到头输出链表
# description:

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    # def printListFromTailToHead(self, listNode):
    #     # write code here
    #     listNode = list(listNode)
    #     if listNode:
    #         return listNode[::-1]
    #     else:
    #         return []


    # 错误的原因是真的把listNode当做是list了，看题不严谨，没有注意到上面的class
    # def printListFromTailToHead(self, listNode):
    #     res = []
    #     for each in listNode:
    #         res.append(each)
    #     return res

    class Solution:
        # 返回从尾部到头部的列表值序列，例如[1,2,3]
        def printListFromTailToHead(self, listNode):
            res = []
            head = listNode
            while head:
                res.insert(0, head.val)
                head = head.next
            return res

if __name__ == '__main__':
    so = Solution()
    print(so.printListFromTailToHead({}))