#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the viralAdvertising function below.
def viralAdvertising(n):
    p = 5
    dayEndLike =0
    for i in range(n):
        dayEndLike += math.floor(p/2)
        p = 3* math.floor(p/2)
    return dayEndLike




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
