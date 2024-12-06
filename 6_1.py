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
    

direcs = [
    (-1,0),
    (0,1),
    (1,0),
    (0,-1),
]

res = 0
with open('inputs/input_6.txt', 'r') as f:
    lines = f.readlines()
    grid = [line[:-1] for line in lines]
    num_r = len(lines)
    num_c = len(lines[0])
    obstacles = set()
    guard = None
    for i, line in enumerate(grid):
        for j, ch in enumerate(line):
            if ch == '#':
                obstacles.add((i,j))
            elif ch == '^':
                guard=(i,j)
    
    # move
    curr_d_idx=0
    visited = set([tuple(guard)])
    while True:
        r, c = guard
        d_r, d_c = direcs[curr_d_idx]
        n_r, n_c = r+d_r, c+d_c
        if not (0<=n_r<num_r and 0<=n_c<num_c):
            break
        elif grid[n_r][n_c] == '#':
            curr_d_idx += 1
            curr_d_idx %= 4
        else:
            guard = (n_r,n_c)
            visited.add(guard)
    
    print(len(visited))
            
            