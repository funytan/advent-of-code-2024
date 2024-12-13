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


def dfs(r, c, peri):
    for i, d in enumerate(direcs):
        d_r, d_c = d
        n_r, n_c=r+d_r, c+d_c
        if ((0<=n_r<num_r) and (0<=n_c<num_c)):
            if grid[n_r][n_c] != grid[r][c]:
                peri[d].append((n_r,n_c))
                
            else:
                if (n_r, n_c) not in visited:
                    visited.add((n_r, n_c))
                    dfs(n_r, n_c, peri)
        else:
            peri[d].append((n_r,n_c))
        


def search(r, c):
    initial_area = len(visited)
    visited.add((r, c))
    peri = defaultdict(list)
    dfs(r,c, peri)
    final_area = len(visited)
    res = sum([len(peri[d]) for d in peri])
    
    for d in peri:
        if d == (0,1) or d == (0,-1):
            ls = sorted(peri[d], key=lambda t: [t[1], t[0]])
            prev = [0,-10]
            for r, c in ls:
                if c == prev[1] and r == prev[0]+1:
                    res -= 1
                prev = [r, c]
        else:
            ls = sorted(peri[d])
            prev = [-10,0]
            for r, c in ls:
                if r == prev[0] and c == prev[1]+1:
                    res -= 1
                prev = [r, c]
    # print(grid[r][c], final_area-initial_area, res)
    return (final_area-initial_area)*res
    
    
res = 0
with open('inputs/input_12.txt', 'r') as f:
    lines = f.readlines()
    grid=[line[:-1] for line in lines]
    num_r=len(grid)
    num_c=len(grid[0])
    for r in range(num_r):
        for c in range(num_c):
            if (r,c) not in visited:
                res+= search(r,c)

            



























        
            