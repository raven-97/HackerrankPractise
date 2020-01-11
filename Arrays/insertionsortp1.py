#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the insertionSort1 function below.
def insertionSort1(n, arr):
    key = arr[n-1]
    f = 0
    for i in range(n-2,-1,-1):
        if arr[i] > key:
            arr[i+1] = arr[i]
        else:
            f = 1
            break
        print(*arr, sep =" ")
    if f == 0:
        arr[i] = key
    else:
        arr[i+1] = key
    print(*arr, sep =" ")


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
