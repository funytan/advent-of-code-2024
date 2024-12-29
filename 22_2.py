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
    curr = ((curr<<6)^curr) % MOD
    # step 2
    curr =  ((curr>>5)^curr) % MOD
    # step 3
    curr =  ((curr<<11)^curr) % MOD
    return curr


res = 0
prices = []
with open('inputs/input_22.txt', 'r') as f:
    lines = f.readlines()
    secret_numbers = list(map(int, [line[:-1] for line in lines]))
    # secret_numbers = [1,2,3,2024]
    for secret in secret_numbers:
        price = [secret%10]
        for _ in range(2000):
            secret = one_iteration(secret)
            price.append(secret%10)
        prices.append(price)

dic = defaultdict(int)
for price in prices:
    price_change = [p_f-p_i for p_f, p_i in zip(price[1:], price)]
    price = price[1:]
    curr = {}
    for i in range(3, len(price)):
        tup = (
            price_change[i-3],
            price_change[i-2],
            price_change[i-1],
            price_change[i],
        )
        if tup not in curr:
            curr[tup] = price[i]
    for tup in curr:
        dic[tup] += curr[tup]
        
        
    
    