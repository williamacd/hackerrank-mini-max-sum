#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    sumarr = []
    total = (0)
    for x in arr:
        total = total + x

    for x in range(0, 5):
        sumarr.insert(x, total - arr[x])

    min = sumarr[0]
    max = sumarr[0]

    for x in sumarr:
        if x < min:
            min = x
        if x > max:
            max = x

    print(str(min)+" "+str(max))

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
