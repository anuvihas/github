#!/bin/python3

import math
import re


# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.


def hourglassSum(arr):
    max_sum = float('-inf')
    for r in range(4):
        for c in range(4):
          current_sum= (arr[r][c]+arr[r][c+1]+arr[r][c+2]+arr[r+1][c+1]+arr[r+2][c]+arr[r+2][c+1]+arr[r+2][c+2])
          max_sum = max(max_sum,current_sum)
    return max_sum

if __name__ == '__main__':
    print("Enter a 6x6 matrix with space :")
    arr = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    result = hourglassSum(arr)
    print("Maximum sum of hourglas :",result)

