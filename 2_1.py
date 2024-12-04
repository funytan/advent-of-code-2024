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

def check(lvl, prev):
    return abs(lvl-prev) >3

ans = 0
with open('inputs/input.txt', 'r') as f:
    lines = f.readlines()
    res = 0
    for idx, line in enumerate(lines, 1):
        report = list(map(int, line.split(' ')))
        prev = report[1]
        if report[0] != report[1] and not check(report[1], report[0]):
            if report[0] > report[1]:
                decreasing = True
            else:
                decreasing = False
            correct = True
            for lvl in report[2:]:
                # print(lvl, prev, report)
                if lvl == prev:
                    correct = False
                    break
                elif prev < lvl:
                    if decreasing or check(lvl, prev):
                        correct = False
                        break
                else:
                    if not decreasing or check(lvl, prev):
                        correct = False
                        break
                prev = lvl
        if correct:
            # print(report)
            ans += 1

print(ans)
                    
                        
                        
            
        