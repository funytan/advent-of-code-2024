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
    (0,-1),
    (-1,0)
]

with open('inputs/input_18.txt', 'r') as f:
    lines = f.readlines()
    falling_bytes = [tuple(map(int, line[:-1].split(','))) for line in lines]
    num_x = 71
    num_y = 71
    obstacles = set(falling_bytes[:1024])
    
    stack = [(0,0)]
    steps = 0
    visited = set(stack)
    check = True
    
    while stack and check:
        new_stack = []
        for x, y in stack:
            if x == 70 and y == 70:
                check=False
                break
            for d_x, d_y in direcs:
                n_x, n_y = x+d_x, y+d_y
                if 0<=n_x<num_x and 0<=n_y<num_y and (n_x, n_y) not in obstacles and (n_x, n_y) not in visited:
                    visited.add((n_x, n_y))
                    new_stack.append((n_x, n_y))
        stack = new_stack
        steps += 1
    
    print(steps-1)
                    
    









        
            