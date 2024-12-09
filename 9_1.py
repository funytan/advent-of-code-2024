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
with open('inputs/input_9.txt', 'r') as f:
    lines = f.readlines()
    s = lines[0][:-1]
    ID = 0
    mem = [-1 for _ in range(len(s)*10)]
    mem_idx = 0
    for i, digit in enumerate(s):
        if i % 2== 0:
            times = int(digit)
            for _ in range(times):
                mem[mem_idx] = ID
                mem_idx += 1
            ID += 1
        else:
            times = int(digit)
            for _ in range(times):
                mem_idx += 1
    
    front = 0
    back = mem_idx -1
    while front <= back:
        if mem[front] != -1:
            front += 1
        elif mem[back] == -1:
            back -=1
        else:
            temp = mem[front]
            mem[front] = mem[back]
            mem[back] = temp
                        
    for idx, ele in enumerate(mem):
        if ele == -1:
            break
        res += idx*ele
    
    print(res)
    
            
        
        
            