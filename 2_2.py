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

def check_diff(curr, prev):
    return abs(curr-prev) >3

def check_report(report):
    if len(report) < 2:
        return False
    curr, prev = report[0], report[1]
    if curr != prev and not check_diff(curr, prev):
        if report[0] > report[1]:
            decreasing = True
        else:
            decreasing = False
        
        for idx, lvl in enumerate(report[2:],2):
            # print(lvl, prev, report)
            if lvl == prev:
                return False, idx
            elif prev < lvl:
                if decreasing or check_diff(lvl, prev):
                    return False, idx
            else:
                if not decreasing or check_diff(lvl, prev):
                    return False, idx
            prev = lvl
        return True, None
    else:
        return False, 1

ans = 0
with open('inputs/input_2.txt', 'r') as f:
    lines = f.readlines()
    res = 0
    for idx, line in enumerate(lines, 1):
        report = list(map(int, line.split(' ')))
        correct, faulty_idx = check_report(report)
        if correct:
            res += 1
        else:
            done = False
            for idx in range(0,2):
                temp = report[:idx] + report[idx+1:]
                correct, _ = check_report(temp)
                if correct:
                    res += 1
                    done=True
                    break
            
            if not done and faulty_idx>1:
                for idx in range(0, len(report)):
                    temp = report[:idx] + report[idx+1:]
                    correct, _ = check_report(temp)
                    if correct:
                        res += 1
                        break
            
print(res)
                    
                        
                        
            
        