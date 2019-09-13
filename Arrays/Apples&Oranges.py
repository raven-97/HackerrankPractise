#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    ainc = 0
    oinc = 0
    for apple in apples:
        apple = apple+a
        if apple >=s and apple <=t:
            ainc = ainc+1
    for orange in oranges:
        orange = orange +b
        if orange >=s and orange <=t :
            oinc =oinc+1

    print(ainc)
    print(oinc)

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
