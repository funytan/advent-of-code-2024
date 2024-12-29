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

res = []

def process_operand(is_literal, operand, a, b, c):
    if is_literal or operand<=3:
        return operand
    elif operand == 4:
        return a
    elif operand == 5:
        return b
    elif operand == 6:
        return c
    else:
        raise ValueError(f"Invalid operand: {operand}")
    

def process_instruction(opcode, operand, a,b,c, instruc_pointer):
    # returns a,b,c and new instruction_pointer
    if opcode == 0: #adv
        val = process_operand(False, operand, a, b, c)
        a = int(a/(2**val))
    elif opcode == 1: #bxl
        val = process_operand(True, operand, a, b, c)
        b = b^val
    elif opcode == 2: #bst     
        val = process_operand(False, operand, a, b, c)
        b = val%8
    elif opcode == 3: #jnz
        if a == 0:
            return a,b,c,instruc_pointer+2
        val = process_operand(True, operand, a, b, c)
        if val != instruc_pointer:
            return a,b,c,val
    elif opcode == 4: #bxc
        b = b^c
    elif opcode == 5: #out
        val = process_operand(False, operand, a, b, c)
        res.append(val%8)
    elif opcode == 6: #bdv
        val = process_operand(False, operand, a, b, c)
        b=int(a/(2**val))
    elif opcode == 7: #cdv
        val = process_operand(False, operand, a, b, c)
        c=int(a/(2**val))
    return a,b,c,instruc_pointer+2

    

with open('inputs/input_17.txt', 'r') as f:
    lines = f.readlines()
    a = int(lines[0][:-1].split(': ')[1])
    b = int(lines[1][:-1].split(': ')[1])
    c = int(lines[2][:-1].split(': ')[1])
    program = lines[4][:-1].split(': ')[1]
    program = list(map(int, program.split(',')))
    instruc_pointer = 0
    while instruc_pointer < len(program):
        # print(a,b,c, instruc_pointer)
        # time.sleep(0.1)
        opcode = program[instruc_pointer]
        operand =  program[instruc_pointer+1]
        a,b,c,instruc_pointer = process_instruction(opcode, operand, a,b,c, instruc_pointer)

print(','.join(list(map(str, res))))



















        
            