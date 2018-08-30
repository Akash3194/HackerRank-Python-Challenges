#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the plusMinus function below.
def plusMinus(arr):
    total_neg = 0
    total_positive = 0
    total_zero = 0
    for i in arr:
        if i > 0:
            total_positive += 1.
        elif i < 0:
            total_neg += 1.
        else:
            total_zero += 1.
    posFrac = round(total_positive / len(arr), 6)
    negFrac = round(total_neg / len(arr), 6)
    zeroFrac = round(total_zero / len(arr), 6)
    print('%r\n%r\n%r' % (posFrac, negFrac, zeroFrac))


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
