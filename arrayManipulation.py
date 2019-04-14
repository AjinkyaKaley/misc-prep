#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
# def arrayManipulation(n, queries):
#     items = [0 for i in range(0,n)]
#     maxValue = -1

#     for q in queries:
#         a = q[0]-1
#         b = q[1]-1
#         k = q[2]
#         while a <= b:
#             items[a]+=k
#             if items[a] >= maxValue:
#                 maxValue = items[a]
#             a+=1
    
#     return maxValue

def arrayManipulation(n,queries):
    arr = [0]*n
    for i in queries:
        arr[i[0] - 1] += i[2]
        arr[i[1]] -= i[2]
    maxval = 0
    itt = 0
    print(arr)
    for q in arr:
        itt += q
        if itt > maxval:
            maxval = itt
    return maxval

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # nm = input().split()

    n = 10

    m = 3

    queries = [[1,5,3],[4,8,7],[6,9,1]]

    # for _ in range(m):
    #     queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)
    print(result)
    # fptr.write(str(result) + '\n')

    # fptr.close()
