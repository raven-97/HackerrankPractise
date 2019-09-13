#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    minlist = list()
    maxlist = list()
    minlist.extend(arr)
    maxlist.extend(arr)

    minlist.remove(max(minlist))
    maxlist.remove(min(maxlist))

    print(sum(minlist),sum(maxlist))


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
