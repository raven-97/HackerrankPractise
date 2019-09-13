#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the luckBalance function below.
def luckBalance(k, contests):
    luck = 0
    imp = list()
    for event in contests:
        luck = luck + event[0]
        if event[1]==1:
            imp.append(event[0])
    
    imp.sort()
    for i in range (len(imp)-k):
        luck = luck - 2*imp[i]
    return luck
    



            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()
