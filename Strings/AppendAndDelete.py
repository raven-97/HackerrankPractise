#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the appendAndDelete function below.
def appendAndDelete(s, t, k):

    f = 1
    cnt = 0
    if k > len(s)+len(t):
        return "Yes"
    for l in range(min(len(s),len(t))):
        if f == 1:
            if s[l] == t[l]:
                cnt += 1
            else:
                f = 0
    if(len(s)+len(t)-2*cnt)>k:
        return "No"
    if(len(s)+len(t)- 2*cnt)%2 == k%2:
        return "Yes"

    else:
        return "No"

                

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
