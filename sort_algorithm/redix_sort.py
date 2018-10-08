# -*- coding: utf-8 -*-
# Author: sunmengxin
# time: 10/7/18
# file: redix_sort.py
# description:

# assign the element into bucket

import numpy as np
import math
def radix_sort(lists, radix=10):
    k = int(math.ceil(math.log(max(lists), radix)))
    bucket = [[] for i in range(radix)]
    for i in range(1, k+1):
        for j in lists:
            bucket[j/(radix**(i-1)) % (radix**i)].append(j)
        del lists[:]
        for z in bucket:
            lists += z
            del z[:]
    return lists


if __name__ == '__main__':
    data = np.random.rand(10)
    data = radix_sort(list(data))
    print(data)