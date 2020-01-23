#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    a = [0]*n
    for j in queries:
        a[j[0]-1] += j[2]
        if j[1] != len(a):
            a[j[1]] -= j[2]
    vmax = 0
    itvar = 0
    for k in a:
        itvar += k
        if itvar > vmax:
            vmax = itvar
    return vmax
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
