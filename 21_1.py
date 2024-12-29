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

# +---+---+---+
# | 7 | 8 | 9 |
# +---+---+---+
# | 4 | 5 | 6 |
# +---+---+---+
# | 1 | 2 | 3 |
# +---+---+---+
#     | 0 | A |
#     +---+---+

num_keypad_keys_to_loc = {
    '7': (0,0),
    '8': (0,1),
    '9': (0,2),
    '4': (1,0),
    '5': (1,1),
    '6': (1,2),
    '1': (2,0),
    '2': (2,1),
    '3': (2,2),
    '0': (3,1),
    'A': (3,2)
}

num_keypad_obstacles = set([(3,0)])


#     +---+---+
#     | ^ | A |
# +---+---+---+
# | < | v | > |
# +---+---+---+

dir_keypad_keys_to_loc = {
    '^': (0,1),
    'A': (0,2),
    '<': (1,0),
    'v': (1,1),
    '>': (1,2),
}

dir_keypad_obstacles = set([(0,0)])

direcs = {
    '>': (0,1),
    'v': (1,0),
    '^': (-1,0),
    '<': (0,-1),
}


def get_shortest_path(start, end, obstacles, num_r, num_c):
    stack = [(start, '')]
    dist = 0
    while stack:
        new_stack = []
        for node, path in stack:
            if node == end:
                return [path for node, path in stack if node==end]
            r, c = node
            for d, d_pos in direcs.items():
                d_r, d_c = d_pos
                n_r, n_c = r+d_r, c+d_c
                if (n_r, n_c) not in obstacles and 0<=r<num_r and 0<=c<num_c:
                    new_stack.append(((n_r, n_c), path+d))
        stack = new_stack
        dist += 1
    raise ValueError('no path found')
    

def solve_numeric_single_step(start_sym, end_sym):
    start = num_keypad_keys_to_loc[start_sym]
    end = num_keypad_keys_to_loc[end_sym]
    return get_shortest_path(start, end, num_keypad_obstacles, 4, 3)
    

def solve_numeric(code):
    prev = 'A'
    paths = ['']
    for ch in code:
        subpaths = solve_numeric_single_step(prev, ch)
        new_paths = []
        for path in paths:
            for subpath in subpaths:
                new_paths.append(path+subpath+'A')
        prev = ch
        paths = new_paths
        # print(paths, subpaths)
    return paths

def solve_direc_single_step(start_sym, end_sym):
    start = dir_keypad_keys_to_loc[start_sym]
    end = dir_keypad_keys_to_loc[end_sym]
    return get_shortest_path(start, end, dir_keypad_obstacles, 4, 3)
    

def solve_direc(code):
    prev = 'A'
    paths = ['']
    for ch in code:
        subpaths = solve_direc_single_step(prev, ch)
        new_paths = []
        for path in paths:
            for subpath in subpaths:
                new_paths.append(path+subpath+'A')
        prev = ch
        paths = new_paths
        # print(paths, subpaths)
    return paths
    
res = 0

with open('inputs/input_21.txt', 'r') as f:
    lines = f.readlines()
    codes = [line[:-1] for line in lines]
    # codes = ['029A'] # remove
    for code in codes:
        paths = solve_numeric(code)
        
        new_paths = []
        for path in paths:
            new_paths+=solve_direc(path)
        min_len = min(len(p) for p in new_paths)
        paths = [p for p in new_paths if len(p) == min_len]
        
        new_paths = []
        for path in paths:
            new_paths+=solve_direc(path)
        min_len = min(len(p) for p in new_paths)
        # max_len = max(len(p) for p in new_paths)
        paths = [p for p in new_paths if len(p) == min_len]
    

        print(min_len, len(paths))
        res += int(code[:-1])*min_len
print(res)
            