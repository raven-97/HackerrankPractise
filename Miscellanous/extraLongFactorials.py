#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the extraLongFactorials function below.
def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*fact(n-1)
def extraLongFactorials(n):
    print(fact(n))


if __name__ == '__main__':
    n = int(input())

    extraLongFactorials(n)
