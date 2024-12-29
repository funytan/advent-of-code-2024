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

res = 0
prices = []
with open('inputs/input_23.txt', 'r') as f:
    lines = f.readlines()
    edges = [line[:-1].split('-') for line in lines]
    adj_dic = defaultdict(set)
    nodes = set()
    for u, v in edges:
        adj_dic[u].add(v)
        adj_dic[v].add(u)
        nodes.add(u)
        nodes.add(v)
    combos = list(combinations(nodes, 3))
    satisfy = []
    for u,v,w in combos:
        if u in adj_dic[v] and u in adj_dic[w] and v in adj_dic[w]:
            satisfy.append((u,v,w))
            if u.startswith('t') or v.startswith('t') or w.startswith('t'):
                res += 1
        
        
    

        
        
    
    