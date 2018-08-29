#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the diagonalDifference function below.
def diagonalDifference(arr):
    s = len(arr) - 1
    ltr = 0
    rtl = 0
    for i in range(s + 1):
        ltr = ltr + arr[i][i] #left to right
        rtl = rtl + arr[i][s - i] #right to left
    return int(math.fabs((ltr - rtl))) #to convert the float value into integer

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
