# -*- coding: utf-8 -*-
# Author: sunmengxin
# time: 10/18/18
# file: 拓扑排序-参考.py
# description:


def indegree0(v,e):
    if v==[]:
        return None

    tmp = v[:]
    for i in e:
        if i[1] in tmp:
            tmp.remove(i[1])
    if tmp==[]:
        return -1

    for t in tmp:
        for i in range(len(e)):
            if t in e[i]:
                e[i]='toDel' #占位，之后删掉
    if e:
        eset=set(e)
        eset.remove('toDel')
        e[:]=list(eset)
    if v:
        for t in tmp:
            v.remove(t)
    return tmp

def topoSort(v,e):
    result=[]
    while True:
        nodes=indegree0(v,e)
        if nodes==None:
            break
        if nodes==-1:
            print('there\'s a circle.')
            return None
        result.extend(nodes)
    return result

if __name__ == '__main__':
    v = ['a', 'b', 'c', 'd', 'e']
    e = [('a', 'b'), ('a', 'd'), ('b', 'c'), ('d', 'c'), ('d', 'e'), ('e', 'c')]
    res = topoSort(v, e)
    print(res)
