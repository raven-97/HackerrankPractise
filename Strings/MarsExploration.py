#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the marsExploration function below.
def marsExploration(s):
    count = 0
    i = 0
    print(count)
    while i < len(s)-2:
        word = s[i:i+3]
        print(word)
        if word[0] != 'S':
            count += 1
        if word[1] != 'O':
            count += 1
        if word[2] != 'S':
            count += 1
        i +=3
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
