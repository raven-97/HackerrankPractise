#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumDistances function below.
def minimumDistances(a):
    d = dict()
    for i in a:
        d[i] = d.get(i,0)+1
    k = list(d.keys())
    v = list(d.values())
    r = list()

    for j in range(len(k)):
        if v[j] >1:
            m = a.index(k[j])
            r.append(a.index(k[j],m+1)-m)
    if len(r) == 0:
        return -1
    return min(r)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()
