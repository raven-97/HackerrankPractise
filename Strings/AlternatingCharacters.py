#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the alternatingCharacters function below.
def alternatingCharacters(s):
    s += " "
    a = list()
    temp =(s[0])
    num = 0
    for i in range(1,len(s)):
        if s[i-1] == s[i]:
            temp = temp+s[i]
        else:
            a.append(temp)
            temp = (s[i])
    #print(a)
    for j in a:
        num +=len(j)-1  
    return num          
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()
