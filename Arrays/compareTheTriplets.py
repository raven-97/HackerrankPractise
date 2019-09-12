#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    al = 0
    bo = 1
    c = [0, 0]

    for i in range(0,len(a)) :
        if a[i] > b[i]:
            c[al] = c[al]+1
        elif a[i] < b[i]:
            c[bo] = c[bo] +1
    
    return c

        



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
