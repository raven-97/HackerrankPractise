#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    # Write your code here
    a.sort()
    #print(a)
    result = list()
    count = dict()
    for i in a:
        count[i] = count.get(i,0)+1
    k = list(count.keys())
    v = list(count.values())
    #print(k)
    #print(v)
    if len(k)==1:
            return v[0]
    for i in range(0,len(k)-1):
        
        if abs(k[i]-k[i+1])<=1:
            result.append(v[i]+v[i+1])
    result.extend(v)
    
    return max(result)

    
        


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
