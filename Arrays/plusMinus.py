#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    plus = 0
    minus = 0
    zeroo = 0
    for element in arr:
        if element < 0: minus = minus+1
        elif element > 0: plus = plus+1
        else:
            zeroo = zeroo+1
    
    print(plus/len(arr))
    print(minus/len(arr))
    print(zeroo/len(arr))


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
