#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the howManyGames function below.
def howManyGames(p, d, m, s):
    n = 0
    if s-p >=0:
        n +=1
        s -=p
    else:
        return 0
    k = (p-m)//d
    if (s -k*p+(k*(k+1)/2)*d) >= 0 :
        s -= (k*p -(k*(k+1)/2)*d)
        n += k
    else:
        x = max(0,(1-2*p/d)+(2/d)*math.sqrt(p*p +d*d/4 - p*d - 2*d*s),(1-2*p/d)-(2/d)*math.sqrt(p*p +d*d/4 - p*d - 2*d*s))
        n += x
        return int(n)
    if s>0:
        n += s//m

    return int(n)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    pdms = input().split()

    p = int(pdms[0])

    d = int(pdms[1])

    m = int(pdms[2])

    s = int(pdms[3])

    answer = howManyGames(p, d, m, s)

    fptr.write(str(answer) + '\n')

    fptr.close()
