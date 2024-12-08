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


def calculate(r1, c1, r2, c2):
    dr = r1-r2
    dc = c1-c2
    return (r1+dr, c1+dc), (r2-dr, c2-dc)

res = set()
with open('inputs/input_8.txt', 'r') as f:
    lines = f.readlines()
    grid = [line[:-1] for line in lines]
    num_r = len(grid)
    num_c = len(grid[-1])
    dic = defaultdict(list)
    for i, row in enumerate(grid):
        for j, ele in enumerate(row):
            if ele != '.':
                dic[grid[i][j]].append((i,j))
    
    for ele in dic:
        idxes = dic[ele]
        for i, loc_1 in enumerate(idxes):
            for j in range(i+1, len(idxes)):
                loc_2 = idxes[j]
                an_1, an_2 = calculate(loc_1[0], loc_1[1], loc_2[0], loc_2[1])
                an_1_x, an_1_y = an_1
                an_2_x, an_2_y = an_2
                if 0<=an_1_x<num_r and 0<=an_1_y<num_c:
                    res.add((an_1_x, an_1_y))
                if 0<=an_2_x<num_r and 0<=an_2_y<num_c:
                    res.add((an_2_x, an_2_y))
                # print(loc_1, loc_2, res)
    print(len(res))
            
        
        
            