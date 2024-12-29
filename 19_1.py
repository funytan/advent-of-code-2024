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

class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.is_end = False
    
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def add_word(self, word):
        curr = self.root
        for ch in word:
            ch_idx = ord(ch)-97
            if curr.children[ch_idx] is None:
                curr.children[ch_idx] = TrieNode()
            curr = curr.children[ch_idx]
        curr.is_end = True
    
    def search_word(self, word):
        curr = self.root
        for idx, ch in enumerate(word):
            ch_idx = ord(ch) - 97 
            curr = curr.children[ch_idx]
            if curr is None:
                yield -1 
                return
            if curr.is_end:
                yield idx 


dp = {}

def search(trie, design, start_idx):
    if (design, start_idx) in dp:
        return dp[(design, start_idx)]
    if start_idx == len(design):
        return True
    ans = False
    for end_idx in trie.search_word(design[start_idx:]):
        if end_idx != -1:
            ans |= search(trie, design, start_idx+end_idx+1)
    dp[(design, start_idx)] = ans
    return ans
    
    

with open('inputs/input_19.txt', 'r') as f:
    lines = f.readlines()    
    towels = lines[0][:-1].split(', ')
    trie = Trie()
    for towel in towels:
        trie.add_word(towel)
    designs  = [line[:-1] for line in lines[2:]]
    
    res = 0
    for design in designs:
        if search(trie, design, 0):
            res += 1
    
print(res)








        
            