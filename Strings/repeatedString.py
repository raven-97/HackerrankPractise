#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def aInString(s,n):
    cnt = 0
    for i in range(n):
            if s[i] == 'a':
                cnt +=1
    return cnt
def repeatedString(s, n):
    cnt =0
    anum = 0
    if len(s) >= n:
        cnt = aInString(s,n)
    else:
        anum = aInString(s,len(s))
        cnt = anum*(n//len(s))
        cnt += aInString(s,n%len(s))

        
    return cnt
    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
