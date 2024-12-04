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

def find_xmas(r,c):
    word = "XMAS"
    if grid[r][c] != word[0]:
        return 0
    ans = 0
    for d_r, d_c in direcs:
        idx = 1
        n_r, n_c = r, c
        found = True
        for _ in range(3):
            n_r, n_c = n_r+d_r, n_c+d_c
            # print(n_r, n_c, idx)
            if 0<=n_r<num_r and 0<=n_c<num_c and grid[n_r][n_c] == word[idx]:
                idx += 1
            else:
                found = False
                break
        if found:
            ans += 1
    return ans
        

res = 0
with open('inputs/input_4.txt', 'r') as f:
    lines = f.readlines()
    grid = [line[:-1] for line in lines]
    num_r = len(lines)
    num_c = len(lines[0])-1
    for r in range(num_r):
        for c in range(num_c):
            res += find_xmas(r,c)
            
print(res)