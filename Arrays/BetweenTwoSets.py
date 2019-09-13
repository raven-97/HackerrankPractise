#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#
def isValid(a, b, candidate):
    for a_ele in a:
        if candidate % a_ele != 0:
            return False
    for b_ele in b:
        if b_ele % candidate != 0:
            return False
    return True


def getTotalX(a, b):
    cnt = 0
    for candidate in range(max(a), min(b)+1):
        if isValid(a, b, candidate):
             cnt += 1
    return cnt
    


    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
