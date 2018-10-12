# -*- coding: utf-8 -*-
# Author: sunmengxin
# time: 10/11/18
# file: 在O(1)时间删除链表节点.py
# description:

import numpy as np
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def delete_node(head,node_deleted):
    # 链表为空
    if head.next == None:
        return

    # 链表只有一个节点
    if head.next == node_deleted:
        head.next = None
        return

    # 要删除的节点不是尾节点
    if node_deleted.next != None:
        node_next = node_deleted.next
        node_deleted.data = node_next.data
        node_deleted.next = node_next.next
        del node_deleted
    else:
        # 要删除的节点是尾节点
        while(head != None):
            if head.next == node_deleted:
                head.next = node_deleted.next
                del node_deleted
                break
            else:
                head = head.next
    return


if __name__ == '__main__':

    data = [1,2,3,4,5,6]
    T = None
    for each in data:
       if T == None:
            T = Node(each)
       else:
           T.next = Node(data)

    new_T = delete_node(T,4)
    while(new_T != None):
        print(new_T.data)
        new_T = new_T.next
