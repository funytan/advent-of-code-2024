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
    [1,0],
    [0,1],
    [1,1],
    [-1,-1],
    [-1,0],
    [0,-1],
    [1,-1],
    [-1,1],
]

def find_x_mas(r,c):
    if grid[r][c]!='A':
        return 0
    if (
         ((grid[r-1][c-1] == 'M' and grid[r+1][c+1] =='S') or (grid[r-1][c-1] == 'S' and grid[r+1][c+1] =='M')) and
         ((grid[r+1][c-1] == 'M' and grid[r-1][c+1] =='S') or (grid[r+1][c-1] == 'S' and grid[r-1][c+1] =='M'))
       ):
        return 1
    return 0

res = 0
with open('inputs/input_4.txt', 'r') as f:
    lines = f.readlines()
    grid = [line[:-1] for line in lines]
    num_r = len(lines)
    num_c = len(lines[0])-1
    for r in range(1, num_r-1):
        for c in range(1, num_c-1):
            res += find_x_mas(r,c)
            
print(res)