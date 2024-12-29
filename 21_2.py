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
import random

all_res = []

direcs_transitions_master = {('^', '^'): [''],
 ('^', 'A'): ['>'],
 ('^', '<'): ['v<'],
 ('^', 'v'): ['v'],
 ('^', '>'): ['>v', 'v>'],
 ('A', '^'): ['<'],
 ('A', 'A'): [''],
 ('A', '<'): ['v<<', '<v<'],
 ('A', 'v'): ['v<', '<v'],
 ('A', '>'): ['v'],
 ('<', '^'): ['>^'],
 ('<', 'A'): ['>>^', '>^>'],
 ('<', '<'): [''],
 ('<', 'v'): ['>'],
 ('<', '>'): ['>>'],
 ('v', '^'): ['^'],
 ('v', 'A'): ['>^', '^>'],
 ('v', '<'): ['<'],
 ('v', 'v'): [''],
 ('v', '>'): ['>'],
 ('>', '^'): ['^<', '<^'],
 ('>', 'A'): ['^'],
 ('>', '<'): ['<<'],
 ('>', 'v'): ['<'],
 ('>', '>'): ['']}

# Extract keys and values
keys = direcs_transitions_master.keys()
values = direcs_transitions_master.values()

# Generate all combinations
combinations = [dict(zip(keys, combo)) for combo in product(*values)]

for direcs_transitions in combinations:

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
    
    
    direcs = {
        '>': (0,1),
        'v': (1,0),
        '^': (-1,0),
        '<': (0,-1),
    }
    
    def get_obstacles(is_numpad):
        if is_numpad:
            return (3,0)
        else:
            return (0,0)
    
    @lru_cache(maxsize=None)
    def get_shortest_path(start, end, num_r, num_c, is_numpad):
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
                    if (n_r, n_c) != get_obstacles(is_numpad) and 0<=r<num_r and 0<=c<num_c:
                        new_stack.append(((n_r, n_c), path+d))
            stack = new_stack
            dist += 1
        raise ValueError('no path found')
        
    
    def solve_numeric_single_step(start_sym, end_sym):
        start = num_keypad_keys_to_loc[start_sym]
        end = num_keypad_keys_to_loc[end_sym]
        return get_shortest_path(start, end, 4, 3, True)
        
    
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
        return get_shortest_path(start, end, 2,3, False)
    
    
    # def solve_direc(code):
    #     prev = 'A'
    #     paths = ['']
    #     for ch in code:
    #         if prev == ch:
    #             subpath = ''
    #         else:
    #             subpath = direcs_transitions[(prev, ch)][0]
    #         new_paths = []
    #         for path in paths:
    #             new_paths.append(path+subpath+'A')
    #         prev = ch
    #         paths = new_paths
    #     return paths
    
    def solve_direc(transitions, path_prefix):
        new_transitions = defaultdict(int)
        # settle path prefix
        optimal_path = direcs_transitions[('A', path_prefix)]
        optimal_path += 'A'
        for u, v in zip(optimal_path, optimal_path[1:]):
            new_transitions[(u, v)] += 1
        path_prefix = optimal_path[0]
        # print(optimal_path)
        # settle other transitions
        for transition, times in transitions.items():
            optimal_path = direcs_transitions[transition]
            optimal_path = 'A' + optimal_path + 'A'
            for u, v in zip(optimal_path, optimal_path[1:]):
                new_transitions[(u, v)] += times
            # print(transition, optimal_path, times)
        return new_transitions, path_prefix
    
    def convert_path_to_transitions(path):
        transitions = defaultdict(int)
        for transition in zip(path, path[1:]):
            transitions[transition]+=1
        return transitions, path[0]
            
    
    def count_and_sort_lengths(path_transitions):
        cnter = Counter()
        for path_transition, prefix in path_transitions:
           cnter[sum(v for k, v in path_transition.items())+1] += 1
        return cnter
    
    res = 0
    
    with open('inputs/input_21.txt', 'r') as f:
        lines = f.readlines()
        codes = [line[:-1] for line in lines]
        # codes = ['029A'] # remove
        all_paths = []
        for code in codes:
            paths = solve_numeric(code)
            paths_transitions = [convert_path_to_transitions(path) for path in paths]
            
            for _ in range(25):
                new_paths_transitions = []
                for transitions, path_prefix in paths_transitions:
                    new_paths_transitions.append(solve_direc(transitions, path_prefix))
                paths_transitions = new_paths_transitions
                cnt = count_and_sort_lengths(paths_transitions)
                
            res += int(code[:-1])*min(k for k in cnt)
    all_res.append(res)

        
            