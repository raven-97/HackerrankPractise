#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the strangeCounter function below.
def strangeCounter(t):
    a = 3
    m = 0
    f = 0
    if t%3 == 0:
        f= 1
        t -= 1
    while( t>=m):
        m = m+ a
        a = 2*a
    print(a)
    if f==1: return m-t
    return m-t+1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    result = strangeCounter(t)

    fptr.write(str(result) + '\n')

    fptr.close()
