#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the organizingContainers function below.
def organizingContainers(container):
    r = list()
    s = list()
    for i in range(len(container)):
        t1 = 0
        t2 = 0
        for j in range(len(container)):
            t1 += container[i][j]
            t2 += container[j][i]
        r.append(t1)
        s.append(t2)
    r.sort()
    s.sort()
    f = 1
    for i in range(len(r)):
        if s[i] != r[i]:
            f = 0
            break

    if f == 1:
        return "Possible"
    else: 
        return "Impossible"
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        container = []

        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))

        result = organizingContainers(container)

        fptr.write(result + '\n')

    fptr.close()
