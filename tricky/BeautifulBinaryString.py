#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulBinaryString function below.
def adjacent(b,m):
    if b.find("010",m+2,m+5) >0:
        return 1
    else:
        return 0
def beautifulBinaryString(b):
    n = 0
    l = list()
    b = b+'     '
    m = b.find('010')
    while(m >= 0):
        l.append(m)
        m = b.find("010",m+1)

    print(l)
    if len(l) == 0:
        return n
    if len(l)== 1:
        return 1
    n = len(l)
    c=0
    f = 0
    for i in range(len(l)-1):

        if l[i+1]-l[i]==2:
            c += 1
            f = 1
        else:
            n -= (c+1)//2
            c = 0
            f =0
    if f==1:
        n -= (c+1)//2

            


    return n
        

        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    b = input()

    result = beautifulBinaryString(b)

    fptr.write(str(result) + '\n')

    fptr.close()
