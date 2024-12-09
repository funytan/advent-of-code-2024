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
    spans = {}
    empties = []
    mem_idx = 0
    for i, digit in enumerate(s):
        if i % 2== 0:
            times = int(digit)
            spans[ID] = [mem_idx, mem_idx+times-1]
            ID += 1
            mem_idx += times
        else:
            times = int(digit)
            if times>0:
                empties.append([mem_idx, mem_idx+times-1])
            mem_idx += times
        
    ID -= 1
    for curr in range(ID,-1,-1):
        print(curr)
        for e_idx, empty in enumerate(empties): 
            s,e=empty
            m_s, m_e = spans[curr]
            if m_e-m_s+1<=e-s+1 and m_s>s:
                spans[curr] = [s, s+m_e-m_s]
                empty[0]=s+m_e-m_s+1
                # print(spans)
                break
    
    idx_to_id = {}
    for ID in spans:
        s, e = spans[ID]
        for idx in range(s,e+1):
            idx_to_id[idx] = ID
    
    for idx in range(mem_idx+1):
        if idx in idx_to_id:
            res += idx_to_id[idx]*idx
    
    print(res)
    
            
        
        
            