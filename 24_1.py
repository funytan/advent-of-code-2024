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
 

def identify_outputs(wire):
    for eq in inp_to_eq[wire]:
        eq_to_inp[eq].remove(wire)
        if len(eq_to_inp[eq]) == 0:
            eqs_to_process.append(eq)
    
def process_eq(in_1, in_2, op):
    if op == 'XOR':
        return in_1^in_2
    elif op == 'AND':
        return in_1 & in_2
    elif op == 'OR':
        return in_1|in_2
    else:
        raise ValueError(f"Unidentified Operation: {op}")


res = None
res_cnt = 0
with open('inputs/input_24.txt', 'r') as f:
    lines = f.readlines()
    wires = {}
    for i, line in enumerate(lines):
        line = line[:-1]
        if not line:
            break
        wire, val = line.split(": ")        
        val = int(val)
        wires[wire] = val
    
    inp_to_eq = defaultdict(list)
    eq_to_inp = {}
    for line in lines[i+1:]:
        line = line[:-1]
        in_1, op, in_2, _, out = line.split(' ')
        eq = (in_1, op, in_2, out)
        inp_to_eq[in_1].append(eq)
        inp_to_eq[in_2].append(eq)
        eq_to_inp[eq] = set([in_1, in_2])
    
    
    eqs_to_process = deque([])
    for wire in wires:
        identify_outputs(wire)
    
    while eqs_to_process:
        in_1, op, in_2, out = eqs_to_process.popleft()
        wires[out] = process_eq(wires[in_1], wires[in_2], op)
        identify_outputs(out)

z_s = sorted([(k, v) for k,v in wires.items() if k[0] == 'z'])[::-1]
print(int(''.join(list(map(str, [item[1] for item in z_s]))),2))
    
        
            
        
    
        
        
        
    

        
        
    
    