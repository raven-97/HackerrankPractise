#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cutTheSticks function below.
def cutTheSticks(arr):
    res = list()
    count = dict()
    m = 0
    for i in arr:
        count[i] = count.get(i,0)+1
    item = list(count.values())

    for i in range(len(item)):
        res.append(len(arr))
        m = min(arr)
        while m in arr:
            arr.remove(m)
        for j in arr:
            j = j-m
    return res
        
 


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
