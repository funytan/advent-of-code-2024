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
 

with open('inputs/input_25.txt', 'r') as f:
    locks = []
    keys = []
    lines = f.readlines()
    for i in range(0,len(lines),8):
        if lines[i][0] == "#":
            is_key = False
        else:
            is_key = True
        heights = defaultdict(int)
        for line in lines[i+1:i+6]:
            # assert len(line) == 6
            for i, ele in enumerate(line[:5]):
                if ele == '#':
                    heights[i] += 1
        if is_key:
            keys.append([heights[i] for i in range(5)])
        else:
            locks.append([heights[i] for i in range(5)])
    
res = 0
for lock in locks:
    for key in keys:
        fit = True
        for i in range(5):
            if lock[i]+key[i]>5:
                fit = False
                break
        if fit:
            res += 1
print(res)
                
            
    
    
    