#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the acmTeam function below.
def acmTeam(topic):
    counts = [0, 0]
    res = ""
    counter = list()
    for i in range(len(topic)-1):
        for j in range(i+1,len(topic)):
            res= str(int(topic[j])+ int(topic[i]))
            counter.append(res.count('1')+res.count('2'))



    counts[0] = max(counter)
    counts[1] = counter.count(counts[0])
    return counts
                


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
