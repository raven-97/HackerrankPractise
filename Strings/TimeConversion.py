#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.

def timeConversion(s):
    time = s.split(':')
    hours = int(time[0])
    minutes = (time[1])
    s = time[2]
    sec = (s[0:2])
    zone = s[2:]
    t = time[0]+time[1]+sec
    if zone == "PM":
        if hours != 12:
            hours = hours+12
    if zone =="AM":
        if t == "120000":
            hours = 0
        if int(t) > 120000:
            hours = 0
        
        

    if hours< 10:
        h= "0" +str(hours)
    else:
        h= str(hours)
    nTime = h+":"+minutes+":"+sec
    return nTime
    
    #
    # Write your code here.
    #

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
