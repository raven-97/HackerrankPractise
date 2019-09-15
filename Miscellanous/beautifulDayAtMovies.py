#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulDays function below.
def beautifulDays(i, j, k):
    result = 0
    for num in range(i,j+1):
        n = num
        revnum = 0
        while n>0:
            revnum = revnum*10 + (n%10)
            n = int(n/10)
        if (revnum-num)%k == 0:
            result += 1
    return result



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ijk = input().split()

    i = int(ijk[0])

    j = int(ijk[1])

    k = int(ijk[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()
