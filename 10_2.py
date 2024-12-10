import io, os, sys
from sys import stdin, stdout
 
# input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
# def input(): return stdin.readline().strip()
# def read_int_list(): return list(map(int, input().split()))
# def read_int_tuple(): return tuple(map(int, input().split()))
# def read_int(): return int(input())
 
from itertools import permutations, chain, combinations, product
from math import factorial, gcd
from collections import Counter, defaultdict, deque
from heapq import heappush, heappop, heapify
from bisect import bisect_left
from functools import lru_cache            
import re


visited = {}
direcs = [
    (0,1),
    (0,-1),
    (1,0),
    (-1,0),
]


def search(r, c):
    next_num = grid[r][c] + 1
    if next_num == 10:
        return 1
    ans = 0
    for d_r, d_c in direcs:
        n_r, n_c = r+d_r, c+d_c
        if 0<=n_r<num_r and 0<=n_c<num_c and grid[n_r][n_c] == next_num:
            if (n_r,n_c) in visited:
                ans += visited[(n_r, n_c)]
            else:
                ans += search(n_r, n_c)
    visited[(r,c)] = ans
    return ans


res = 0
with open('inputs/input_10.txt', 'r') as f:
    lines = f.readlines()
    grid= [list(map(int, line[:-1])) for line in lines]
    num_r = len(grid[0])
    num_c = len(grid[1])
    
    for i, row in enumerate(grid):
        for j, ele in enumerate(row):
            if ele == 0:
                res += search(i, j)
    print(res)    
            
        
        
            