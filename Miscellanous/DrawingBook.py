#!/bin/python3

import os
import sys
import math
#
# Complete the pageCount function below.
#
def pageCount(n, p):
    turn =[0,0]
    if n ==2:
        return 0

    if n%2 ==0:
        if p == n-1:
            return 1

    turn[0] = int(math.ceil((p-1)/2))
    turn [1] = int(math.floor((n-p)/2))



    return min(turn[0],turn[1])
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
