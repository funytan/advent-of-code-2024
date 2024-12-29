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
import time
import random

MOD = 16777216

def one_iteration(secret):
    curr = secret
    # step 1
    curr = ((curr*64)^curr) % MOD
    # step 2
    curr =  ((curr//32)^curr) % MOD
    # step 3
    curr =  ((curr*2048)^curr) % MOD
    return curr

res = 0
with open('inputs/input_22.txt', 'r') as f:
    lines = f.readlines()
    secret_numbers = list(map(int, [line[:-1] for line in lines]))
    # secret_numbers = [1]
    for secret in secret_numbers:
        for _ in range(2000):
            secret = one_iteration(secret)
        res += secret
    
    
    