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
    


res = 0
with open('inputs/input_5.txt', 'r') as f:
    lines = f.readlines()
    lines = [line[:-1] for line in lines]
    rules = defaultdict(set)
    for idx, line in enumerate(lines):
        if line != '':
            x, y = list(map(int, line.split('|')))
            rules[y].add(x)
        else:
            break
        
    updates = []
    res = 0
    for line in lines[idx+1:]:
        update = list(map(int, line.split(',')))
        unallowable_set = set()
        right_order = True
        for i, num in enumerate(update):
            if num in unallowable_set:
                right_order = False
                for j, prev_num in enumerate(update[:i]):
                    if num in rules[prev_num]:
                        update[i], update[j] = update[j], update[i]
                # print(update)
            unallowable_set = unallowable_set.union(rules[num])
            
        if not right_order:
            # print(update)
            res += update[len(update)//2]
    
    print(res)
            
    