#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the workbook function below.


    
def workbook(n, k, arr):
    pg = 0
    res = 0
    for i in range(n):
        pg += 1
        prb = 1
        while arr[i] > 0:
            arr[i] -= 1
            if pg == prb:
                res += 1
            if prb % k == 0 and arr[i] != 0:
                pg += 1
            prb +=1
    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = workbook(n, k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
