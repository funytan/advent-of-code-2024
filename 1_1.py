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


            
with open('inputs/input_1.txt', 'r') as f:
    lines = f.readlines()
    res = 0
    left = []
    right = []
    for line in lines:
        l, r = list(map(int, line.split()))
        left.append(l)
        right.append(r)
    for l, r in zip(sorted(left), sorted(right)):
        res += abs(l-r)
    print(res)