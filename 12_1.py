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


visited = set()
res = []
direcs = [
    (0,1),
    (0,-1),
    (1,0),
    (-1,0),
]

def dfs(r, c):
    peri, area = 0, 1
    for d_r, d_c in direcs:
        n_r, n_c=r+d_r, c+d_c
        if ((0<=n_r<num_r) and (0<=n_c<num_c)):
            if grid[n_r][n_c] != grid[r][c]:
                peri += 1
            else:
                if (n_r, n_c) not in visited:
                    visited.add((n_r, n_c))
                    n_peri, n_area = dfs(n_r, n_c)
                    area += n_area
                    peri += n_peri
        else:
            peri += 1
    return peri, area
        


def search(r, c):
    visited.add((r, c))
    peri, area = dfs(r,c)
    res.append((peri, area))
    
    
    



with open('inputs/input_12.txt', 'r') as f:
    lines = f.readlines()
    grid=[line[:-1] for line in lines]
    num_r=len(grid)
    num_c=len(grid[0])
    for r in range(num_r):
        for c in range(num_c):
            if (r,c) not in visited:
                visited.add((r,c))
                search(r,c)
    

print(sum([i[0]*i[1] for i in res]))
        
            