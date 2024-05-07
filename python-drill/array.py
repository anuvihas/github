'''

An array is a type of data structure that stores elements of the same type
in a contiguous block of memory. In an array, A, of size N, each memory location 
has some unique index, i(where 0<i<N), that can be referenced as A[i].

reverseArray has the following parameter(s):
input:
int A[n]: the array to reverse

output:
int[n]: the reversed array

'''


def reverseArray(arr):
    arr.reverse()
    return arr

def main():
    arr = list(map(int, input().split()))
    array = reverseArray(arr)
    print(' '.join(map(str, array)))

if __name__ == "__main__":
    main()
