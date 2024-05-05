""""
Given a  2D Array, arr:

1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
An hourglass in  is a subset of values with indices falling in this pattern in arr's graphical representation:

a b c
  d
e f g

There are 16 hourglasses in arr. An hourglass sum is the sum of an hourglass' values. Calculate the hourglass sum for every hourglass in arr , then print the maximum hourglass sum. The array will always be 6 x 6 .

"""
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

