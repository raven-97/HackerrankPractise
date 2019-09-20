#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the squares function below.
def squares(a, b):
    cnt = 0
    sq = 0
    for i in range(a,b+1):
        sq = math.sqrt(i)
        if sq - int(sq) == 0:
            break
    if sq - int(sq) != 0:
        return 0
    print("count 1",cnt)
    for j in range(int(sq),b+1):
        if j*j <= b:
            cnt += 1
        else:
            break
    print("count 2",cnt)

    return cnt


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        ab = input().split()

        a = int(ab[0])

        b = int(ab[1])

        result = squares(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
