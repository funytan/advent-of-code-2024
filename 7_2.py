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
    


def test(curr, idx):
    if idx == len(eq):
        if curr == test_val:
            return True
        else:
            return False
    num = eq[idx]
    return test(curr*num, idx+1) or test(curr+num, idx+1) or test(int(str(curr)+str(num)), idx+1)
    

res = 0
with open('inputs/input_7.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        test_val, eq = line[:-1].split(": ")
        test_val = int(test_val)
        eq = list(map(int, eq.split(" ")))
        if test(eq[0], 1):
            res += test_val

print(res)
        
            