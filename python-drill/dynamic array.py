"""
Complete the dynamicArray function below.

dynamicArray has the following parameters:
- int n: the number of empty arrays to initialize in arr
- string queries[q]: query strings that contain 3 space-separated integers

Returns

int[]: the results of each type 2 query in the order they are presented

Sample Input
2 5
1 0 5
1 1 7
1 0 3
2 1 0
2 1 1

Sample Output
7
3

"""



import math
import re

#
# Complete the 'dynamicArray' function below.
#
# The f unction is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n, queries):
    seqlist=[[] for i in range(n)]
    lastAnswer=0
    result=[]
    for q in queries:
        if q[0]==1:
            seq=(q[1]^ lastAnswer)%n
            seqlist[seq].append(q[2])
        else:
            seq=(q[1]^ lastAnswer)%n
            lastAnswer=seqlist[seq][q[2]%len(seqlist[seq])]
            result.append(lastAnswer)
    return result

if __name__ == '__main__':
    first_multiple_input = input("Values :").rstrip().split()
    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)
    print(result)

