#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the insertionSort2 function below.
def insertionSort2(n, a):
    for i in range(1,n):
        key = a[i]
        j = i-1

        while j >= 0 and a[j] > key:
            a[j+1] = a[j]
            j = j-1
        a[j+1] = key
        print(*a, sep=' ')
    


if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    insertionSort2(n, a)
