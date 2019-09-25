#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the queensAttack function below.
def queensAttack(n, k, rq, cq, obstacles):
    count = 0
    board = list()
    board = [[0 for x in range(n)] for y in range(n)]
    for i in range(k):
        board[obstacles[i][0]-1][obstacles[i][1]-1] = 1
    print(board)
    f1 = 0
    f2 = 0
    f3 = 0
    f4 = 0
    f5 = 0
    f6 = 0
    f7 = 0
    f8 = 0
    rq -= 1
    cq -= 1
    if cq ==0 or cq == n or rq ==0 or rq == n:
        k = n//2 +1
    else: k = n+2

    for i in range(1,k):
        if rq - i >= 0 and f1 == 0:
            if board[rq - i][cq] == 0:
                count += 1
            else:f1 = 1
        if rq + i < n and f2 == 0:
            if board[rq + i][cq] == 0:
                count += 1
            else:f2 = 1
        if cq - i >= 0 and f3 == 0:
            if board[rq][cq - i] == 0:
                count += 1
            else:f3 = 1
        if cq + i < n and f4 == 0:
            if board[rq][cq + i] == 0:
                count += 1
            else:f4 = 1
        if rq - i >= 0 and cq - i >= 0 and f5 ==0:
            if board[rq-i][cq-i] == 0:
                count += 1
            else:f5 = 1
        if rq + i < n and cq + i < n and f6 ==0:
            if board[rq+i][cq+i] == 0:
                count += 1
            else:f6 = 1
        if rq - i >= 0 and cq + i < n and f7 ==0:
            if board[rq-i][cq-i] == 0:
                count += 1
            else:f7 = 1
        if rq + i < n and cq - i >=0 and f8 ==0:
            if board[rq+i][cq+i] == 0:
                count += 1
            else:f8 = 1
                

    return count
 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    r_qC_q = input().split()

    r_q = int(r_qC_q[0])

    c_q = int(r_qC_q[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()
