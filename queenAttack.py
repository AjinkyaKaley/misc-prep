#!/bin/python3

import math
import os
import random
import re
import sys
# Complete the queensAttack function below.
def queensAttack(n, k, r_q, c_q, obstacles):
    counter = 0
    visited = [[False for i in range(n)]for j in range(n)]
    # visited[r_q][c_q] = True
    return helper(n, k, r_q, c_q, obstacles, counter,visited)


def helper(n, k, r_q, c_q, obstacles, counter, visited):

    if r_q >= n or c_q >= n or obstaclesCheck(r_q,c_q,obstacles):
        return counter

    if visited[r_q][c_q]:
        return counter

    visited[r_q][c_q] = True

    counter = helper(n, k, r_q+1, c_q, obstacles, counter+1,visited)
    counter = helper(n, k, r_q-1, c_q, obstacles, counter+1,visited)
    counter = helper(n, k, r_q, c_q+1, obstacles, counter+1,visited)
    counter = helper(n, k, r_q, c_q-1, obstacles, counter+1,visited)
    counter = helper(n, k, r_q+1, c_q+1, obstacles, counter+1,visited)
    counter = helper(n, k, r_q-1, c_q-1, obstacles, counter+1,visited)
    counter = helper(n, k, r_q+1, c_q-1, obstacles, counter+1,visited)
    counter = helper(n, k, r_q-1, c_q+1, obstacles, counter+1,visited)
    return counter

def obstaclesCheck(r_q,c_q,obstacles):
    for pair in obstacles:
        if r_q == pair[0] and c_q == pair[1]:
            return True
    return False

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # nk = input().split()

    n = 5

    k = 3

    # r_qC_q = input().split()

    r_q = 4

    c_q = 3

    obstacles = [[5,5],[4,2],[2,3]]
    # for _ in range(k):
    #     obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)
    print(result)
    # fptr.write(str(result) + '\n')

    # fptr.close()
