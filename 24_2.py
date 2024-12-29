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

def convert_wires_to_bin(ls):
    ls = sorted(ls)[::-1]
    return ''.join(list(map(str, [item[1] for item in ls])))


x_s = []
y_s = []
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
    
    for wire, val in wires.items():
        if wire[0] == 'x':
            x_s.append((wire, val))
        else:
            y_s.append((wire, val))
    x_s = convert_wires_to_bin(x_s)
    y_s = convert_wires_to_bin(y_s)
        
    
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
    # for wire in wires:
    #     identify_outputs(wire)
    # identify_outputs('x00')
    # identify_outputs('y00')
    
    # by inspection
    for i in range(46):
        wire_num = "{:02d}".format(i)
        print(f"wire_num: {wire_num}")
        identify_outputs(f'x{wire_num}')
        identify_outputs(f'y{wire_num}')
        while eqs_to_process:
            in_1, op, in_2, out = eqs_to_process.popleft()
            print(in_1, op, in_2, out)
            wires[out] = process_eq(wires[in_1], wires[in_2], op)
            identify_outputs(out)
        # input()

# z_s = sorted([(k, v) for k,v in wires.items() if k[0] == 'z'])[::-1]
# z_s = convert_wires_to_bin(z_s)
# print(z_s)
# print(x_s)
# print(y_s)
# org = bin(int(x_s, 2) + int(y_s, 2))[2:]
# print(org)

# res = 0
# for i, j in zip(z_s, org):
#     if i!=j:
#         res += 1
    

# x00 XOR y00 = z00
# x00 AND y00 = ktt (carry_0)

# x01 XOR y01 = rvb (int_1_1)
# ktt XOR rvb = z01 
# ktt AND rvb = kmb (int_1_2)
# x01 AND y01 -> kgp (int_1_3)
# kgp OR kmb -> rkn (carry_1)
# 

# njf XOR jsb djg
# jsb AND njf z12

# x19 AND y19 z19
# qjc XOR kbs sbg
            
# y24 AND x24 hjm
# x24 XOR y24 mcq
    
# spj OR gqf z37
# hhp XOR tjm dsd

res = [
   "djg", "z12", "z19", "sbg", "hjm", "mcq", "z37", "dsd"
]
    

        
        
    
    