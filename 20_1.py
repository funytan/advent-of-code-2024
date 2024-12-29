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
import time


direcs = [
    (0,1),
    (1,0),
    (-1,0),
    (0,-1),
]


obstacles=set()

def solve(start, end, num_r, num_c, obstacles):
    stack = [start]
    visited = set([start])
    time_elapsed = 0
    found = False
    while stack:
        new_stack = []
        for r, c in stack:
            if (r,c) == end:
                found=True
                break
            for d_r, d_c in direcs:
                n_r, n_c = r+d_r, c+d_c
                if 0<=n_r<num_r and 0<=n_c<num_c and (n_r, n_c) not in visited:
                    if (n_r, n_c) not in obstacles:
                        visited.add((n_r, n_c))
                        new_stack.append((n_r, n_c))
        stack = new_stack
        if not found:
            time_elapsed += 1
    return time_elapsed


with open('inputs/input_20.txt', 'r') as f:
    lines = f.readlines()
    grid = [line[:-1] for line in lines]
    num_r = len(grid)
    num_c = len(grid[0])
    for r in range(num_r):
        for c in range(num_c):
            if grid[r][c] == '#':
                obstacles.add((r,c))
            elif grid[r][c] == 'S':
                start = (r,c)
            elif grid[r][c] == 'E':
                end = (r,c)
    
original_time = solve(start, end, num_r, num_c, obstacles)
res = 0
dic = defaultdict(int)

for r in range(num_r):
    print(r)
    for c in range(num_c):
        if (r,c) in obstacles:
            obstacles.remove((r,c))
            elapsed = solve(start, end, num_r, num_c, obstacles)
            dic[original_time-elapsed] += 1
            if (elapsed+100)<=original_time:
                res += 1
            obstacles.add((r,c))

        
# res = 0        
    
# stack = [(start[0], start[1], -1, -1, -1,- -1)]
# visited = set([(start[0], start[1], -1, -1, -1,- -1)])
# curr_time = 0
# while stack and curr_time<=(original_time-100):
#     new_stack = []
#     for r, c, o_r, o_c, f_r, f_c in stack:
#         for d_r, d_c in direcs:
#             n_r, n_c = r+d_r, c+d_c
#             if 0<=n_r<num_r and 0<=n_c<num_c:
#                 if n_r, n_c in obstacles:
#                     if o_r == -1:
#                         r, c, o_r, o_c, f_r, f_c
                
                
                
#                 if c1r!=-1 and c2r==-1: #compulsory usage
#                     if (n_r, n_c, c1r, c1c, n_r, n_c) not in visited:
#                         visited.add((n_r, n_c, c1r, c1c, n_r, n_c))
#                         new_stack.append((n_r, n_c, c1r, c1c, n_r, n_c))
#                 else:
#                     if (n_r, n_c, c1r, c1c, c2r, c2c) not in visited and (n_r, n_c) not in obstacles:
#                         visited.add((n_r, n_c, c1r, c1c, c2r, c2c))
#                         new_stack.append((n_r, n_c, c1r, c1c, c2r, c2c))
#                     if c1r == -1:
#                         if (n_r, n_c, n_r, n_c, -1, -1) not in visited:
#                             visited.add((n_r, n_c, n_r, n_c, -1, -1))
#                             new_stack.append((n_r, n_c, n_r, n_c, -1, -1))

                
                
                
                
                
    #             if (n_r, n_c) not in obstacles:
    #                 if (n_r, n_c, c, c1r, c1c, c2r, c2c) not in visited:
    #                     visited.add((n_r, n_c, c1r, c1c, c2r, c2c))
    #                     new_stack.append((n_r, n_c, c1r, c1c, c2r, c2c))
    #             else:
    #                 if c1r!= -1:
    #                     c1r = n_r
    # stack = new_stack
    # curr_time += 1









# res = 0
# dic = defaultdict(int)

# # horizontal   
# for r in range(num_r):
#     print(r)
#     for c in range(num_c-1):
#         removed = []
#         if (r,c) in obstacles and (r, c+1) not in obstacles:
#             obstacles.remove((r,c))
#             removed.append((r,c))
#         if (r,c+1) in obstacles and (r, c):
#             obstacles.remove((r,c+1))
#             removed.append((r,c+1))
#         if not removed:
#             continue
#         elapsed = solve(start, end, num_r, num_c, obstacles)
#         dic[original_time-elapsed] += 1
#         if (elapsed+100)<=original_time:
#             res += 1
#         for node in removed:
#             obstacles.add(node)

# # vertical
# for r in range(num_r-1):
#     print(r)
#     for c in range(num_c):
#         removed = []
#         if (r,c) in obstacles:
#             obstacles.remove((r,c))
#             removed.append((r,c))
#         if (r+1,c) in obstacles:
#             obstacles.remove((r+1,c))
#             removed.append((r+1,c))
#         if not removed:
#             continue
#         elapsed = solve(start, end, num_r, num_c, obstacles)
#         dic[original_time-elapsed] += 1
#         if (elapsed+100)<=original_time:
#             res += 1
#         for node in removed:
#             obstacles.add(node)
# print(res)


        
            