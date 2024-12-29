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
    (0,1), # E
    (1,0), # S
    (0,-1), # W
    (-1,0), # N
]

def check(n_r, n_c, direc_idx, add_cost):
    if (n_r, n_c, direc_idx) not in visited and 0<=n_r<num_r and 0<=n_c<num_c and grid[n_r][n_c] != '#':
        visited.add((n_r, n_c, direc_idx))
        heappush(heap, (dist+add_cost, (n_r, n_c), direc_idx))
    
    
res = 0
with open('inputs/input_16.txt', 'r') as f:
    lines = f.readlines()
    grid=[line[:-1] for line in lines]
    num_r=len(grid)
    num_c=len(grid[0])
    start, end  = None, None
    for r in range(num_r):
        for c in range(num_c):
            if grid[r][c] == 'S':
                start = (r,c)
            elif grid[r][c] == 'E':
                end = (r,c)
    heap=[(0, start, 0)]
    visited = set([(start[0], start[1], 0)])
    heapify(heap)
    
    while heap:
        # print(heap)
        dist, node, direc_idx = heappop(heap)
        if node == end:
            break
        r, c = node
        check(r+direcs[direc_idx][0], c+direcs[direc_idx][1], direc_idx, 1) # forward
        direc_idx += 1
        direc_idx %=4
        check(r+direcs[direc_idx][0], c+direcs[direc_idx][1], direc_idx, 1001) # cw
        direc_idx -= 2
        direc_idx %=4
        check(r+direcs[direc_idx][0], c+direcs[direc_idx][1], direc_idx, 1001) # ccw
        

    print(dist)
    



















        
            