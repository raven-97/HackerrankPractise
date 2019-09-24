#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    cnt = 0
    f = 0
    while f < len(c)-1:
        if f >= len(c)-2:
            break
        if c[f+2] == 0:
            f +=2
        elif c[f+1] == 0:
            f += 1
        cnt += 1
        if f >= len(c)-1:
            break
    if f+1 == len(c)-1:
        cnt += 1
        
    return cnt




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
