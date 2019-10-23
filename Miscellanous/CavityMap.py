#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cavityMap function below.
def cavityMap(grid):
    res = list()
    res.append(grid[0])
    for i in range(1, len(grid)-1):
        word = grid[i][0]
        for j in range(1, len(grid[i])-1):
            if grid[i][j]> grid[i-1][j] and grid[i][j] > grid[i+1][j] and grid[i][j] > grid[i][j-1] and grid[i][j] > grid[i][j+1]:
                word = word + 'X'
            else:
                word = word + grid[i][j]
        word = word +grid[i][len(grid[i])-1]
        res.append(word)
    if len(grid) > 1:
        res.append(grid[len(grid)-1])
    return res
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = cavityMap(grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
