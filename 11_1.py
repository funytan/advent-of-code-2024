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


# visited = {}
# direcs = [
#     (0,1),
#     (0,-1),
#     (1,0),
#     (-1,0),
# ]


# def search(r, c):



res = 0
with open('inputs/input_11.txt', 'r') as f:
    lines = f.readlines()
    curr= list(map(int, lines[0][:-1].split()))
    curr = Counter(curr)
    for i in range(25):
        print(i)
        new_curr = defaultdict(int)
        for k, v in curr.items():
            if k == 0:
                new_curr[1] += v
            elif len(str(k)) % 2 == 0:
                n =len(str(k))
                left = str(k)[:n//2]
                right = str(k)[n//2:]
                new_curr[int(left)] += v
                new_curr[int(right)] += v
            else:
                new_curr[k*2024] += v
                
        curr = new_curr
        # print(curr)
    print(sum([v for k,v in curr.items()]))    
        
        
            