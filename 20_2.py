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
JUMP_DIST = 20
SAVED = 100
dist_to_end = defaultdict(int)


def solve(start, end, num_r, num_c, obstacles):
    stack = [start]
    visited = set([start])
    time_elapsed = 0
    found = False
    while stack:
        dist_to_end[stack[0]] = time_elapsed
        assert len(stack) == 1
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

@lru_cache(maxsize=None)
def get_jumps(r, c):
    stack = [(r,c)]
    dist = 0
    ans = {}
    new_visited = set(stack)
    while stack and dist<JUMP_DIST:
        new_stack = []
        for r,c in stack:
            for d_r, d_c in direcs:
                n_r, n_c = r+d_r, c+d_c
                if 0<=n_r<num_r and 0<=n_c<num_c and (n_r, n_c) not in new_visited:
                    new_visited.add((n_r, n_c))
                    new_stack.append((n_r, n_c))
                    if (n_r, n_c) not in obstacles:
                        if (n_r, n_c) not in ans:
                            ans[(n_r, n_c)] = dist+1
                        
        dist += 1
        stack = new_stack
    # print(r,c,ans)
    # assert 1==2
    return [(dist, node) for node, dist in ans.items()]


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
for node in dist_to_end:
    dist_to_end[node] = original_time - dist_to_end[node]
cutoff = original_time-SAVED


heap = [(0, start,False,None,None)]
heapify(heap)
res = 0
dic = defaultdict(int)
visited = set(heap)
thres = 0
jumped_set = set()

while heap and heap[0][0]<=cutoff:
    dist, curr, jumped, jump_start, jump_end = heappop(heap)
    if dist > thres:
        thres = dist
        if dist%100 == 0 :
            print(dist)
    r,c = curr
    if curr == end:
        dic[original_time-dist] += 1
        res += 1
    for d_r, d_c in direcs:
        n_r, n_c = r+d_r, c+d_c
        if 0<=n_r<num_r and 0<=n_c<num_c:
            ele = (dist+1, (n_r,n_c), jumped, jump_start, jump_end)
            if (n_r, n_c) not in obstacles and ((n_r,n_c), jumped, jump_start, jump_end) not in visited:
                heappush(
                    heap,
                    ele
                )
                visited.add(
                    ((n_r,n_c), jumped, jump_start, jump_end)
                )
    if not jumped:
        jumps = get_jumps(r, c)
        for jump_dist, jump_end in jumps:
            final_dist = dist+jump_dist+dist_to_end[jump_end]
            if (curr, jump_end) not in jumped_set:
                jumped_set.add(
                    (curr, jump_end)
                )
                if final_dist<=cutoff:
                    dic[original_time-final_dist] += 1
                    res += 1
            
print(res)

            # ele = (dist+jump_dist, jump_end, True, (r, c), jump_end)
            # if ele[1] not in obstacles and (jump_end, True, (r,c), jump_end) not in visited:
            #     heappush(
            #         heap,
            #         ele
            #     )
            #     visited.add(
            #         (jump_end, True, (r,c), jump_end)
            #     )


# print(res)
       
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


        
            