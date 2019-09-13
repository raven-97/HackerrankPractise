#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    counts = dict()
    arr.sort()
    

    for element in arr:
        counts[element] = counts.get(element,0)+1
    v = list(counts.values())
    k = list(counts.keys())

    return k[v.index(max(v))]

    




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
