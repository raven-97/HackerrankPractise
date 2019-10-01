#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the encryption function below.
def encryption(s):
    s.replace(" ","")
    l = math.ceil(math.sqrt(len(s)))
    r = math.floor(math.sqrt(len(s)))
    while (l*r < len(s)):
        if l < r:
            l += 1
        else:
            r += 1
    c = max(l,r)
    a = [["" for m in range(c)]for k in range(c)]
    z = 0
    for i in range(r):
        for j in range(l):
            if z < len(s):
                a[i][j] += s[z]
                z += 1
            
    S = ""
    for i in range(c):
        for j in range(c):
            S += a[j][i]
        S += " "


    return S


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
