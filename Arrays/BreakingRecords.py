#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    low = scores[0]
    high = scores[0]
    count = [0,0]
    for score in scores:
        if score > high:
            count[0] +=1
            high = score
        if score < low:
            count[1] +=1
            low = score
    
    return count
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
