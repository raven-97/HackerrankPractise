#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    
    res = list()
 
  
    for i in alice:
        temp = list()
        temp.append(i)
        temp.extend(scores)
        temp.sort(reverse=True)
        rank = dict()
        for j in temp:
            rank[j]= rank.get(j,0)+1
        k = list(rank.keys())
        for h in range(len(k)):
            if i == k[h]:
                res.append(h+1)
    return res


    


    

   

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
