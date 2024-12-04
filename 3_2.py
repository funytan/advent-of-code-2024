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


pattern = "mul\((\d{1,3}),(\d{1,3})\)"
def process(line):
    matches = re.findall(pattern, line)
    return sum([int(a)*int(b) for a, b in matches])


res = 0
with open('inputs/input_3.txt', 'r') as f:
    lines = f.readlines()
    lines = '\n'.join(lines)
    do_lines = lines.split('do()')
    for do_line in do_lines:
        do_portion = do_line.split("don't()")[0]
        res += process(do_portion)
            
print(res)