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
 


res = None
res_cnt = 0
with open('inputs/input_23.txt', 'r') as f:
    lines = f.readlines()
    edges = [line[:-1].split('-') for line in lines]
    adj_dic = {}
    nodes = set()
    for u, v in edges:
        if u not in adj_dic:
            adj_dic[u] = set()
        if v not in adj_dic:
            adj_dic[v] = set()
        adj_dic[u].add(v)
        adj_dic[v].add(u)
        nodes.add(u)
        nodes.add(v)
    
    for node, connected_nodes in adj_dic.items():
        ls = list(connected_nodes)+[node]
        # print(len(ls))
        for size in range(4, len(ls)+1):
            combos = list(combinations(ls, size))
            for combo in combos:
                check = True
                for i, node in enumerate(combo):
                    other_nodes = combo[:i]+combo[i+1:]
                    for other_node in other_nodes:
                        if other_node not in adj_dic[node]:
                            check =False
                            break
                    if not check:
                        break
                if check:
                    if size > res_cnt:
                        res_cnt= size
                        res = combo
                    break
            if not check:
                break
                

            
    
    # combos = list(combinations(nodes, 3))
    # for u,v,w in combos:
    #     if u in adj_dic[v] and u in adj_dic[w] and v in adj_dic[w]:
    #         if u.startswith('t') or v.startswith('t') or w.startswith('t'):
    #             res += 1
        
        
    

        
        
    
    