#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kaprekarNumbers function below.
def kaprekarNumbers(p, q):
    f = 0
    for i in range(p,q+1):
        if i == 3 or i ==2: continue
        if i == 1:
            print(i, end = " ")
            f = 1
            continue
        s = str(i)
        ss = str(i*i)
        l = ss[:len(ss)-len(s)]
        r = ss[len(ss)-len(s):]
        try:
            if int(l)+int(r) == i:
                f = 1
                print(i, end = " ")
        except:
            print(l,r)
    if f == 0:
        print("INVALID RANGE")

if __name__ == '__main__':
    p = int(input())

    q = int(input())

    kaprekarNumbers(p, q)

