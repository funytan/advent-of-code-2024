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

def check(r, c, original_direc_idx, n_r, n_c, direc_idx, add_cost, dist):
    if (n_r, n_c, direc_idx) not in visited and 0<=n_r<num_r and 0<=n_c<num_c and grid[n_r][n_c] != '#':
        visited[(n_r, n_c, direc_idx)] = dist+add_cost
        heappush(heap, (dist+add_cost, (n_r, n_c), direc_idx))
        store[(n_r, n_c, direc_idx)].add((r,c,original_direc_idx))
    elif (n_r, n_c, direc_idx) in visited and (dist+add_cost) == visited[(n_r, n_c, direc_idx)]:
        store[(n_r, n_c, direc_idx)].add((r,c,original_direc_idx))
        
def draw():
    for r in range(num_r):
        row = []
        for c in range(num_c):
            if grid[r][c] == '.':
                row.append('.')
            elif grid[r][c] == '#':
                row.append('#')
            else:
                row.append('O')
        print(''.join(row))
    
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
    visited = {(start[0], start[1], 0): 0}
    store = defaultdict(set)
    heapify(heap)
    done_dist = None
    done_direcs = []
    while heap:
        # print(heap)
        dist, node, direc_idx = heappop(heap)
        if node == end:
            if done_dist is None:
                done_dist = dist
            if dist == done_dist:
                done_direcs.append(direc_idx)
            else:
                break
            
        r, c = node
        check(r, c, direc_idx, r+direcs[direc_idx][0], c+direcs[direc_idx][1], direc_idx, 1, dist) # forward
        check(r, c, direc_idx, r+direcs[(direc_idx+1)%4][0], c+direcs[(direc_idx+1)%4][1], (direc_idx+1)%4, 1001, dist) # cw
        check(r, c, direc_idx, r+direcs[(direc_idx-1)%4][0], c+direcs[(direc_idx-1)%4][1], (direc_idx-1)%4, 1001, dist) # ccw
        

deq = deque([(end[0], end[1], direc_idx) for direc_idx in done_direcs])
res = set(deq)
while deq:
    node = deq.popleft()
    for n_node in store[node]:
        if n_node not in res:
            res.add((n_node[0], n_node[1]))
            deq.append(n_node)
print(len(res))
# draw()
    
    



















        
            