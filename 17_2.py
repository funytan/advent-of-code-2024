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
        print(a,b,c, instruc_pointer)
        # time.sleep(0.1)
        opcode = program[instruc_pointer]
        operand =  program[instruc_pointer+1]
        a,b,c,instruc_pointer = process_instruction(opcode, operand, a,b,c, instruc_pointer)

print(','.join(list(map(str, res))))

def run_once(num):
    curr = 0
    global res
    res = []
    a = num
    b = 0
    c = 0
    instruc_pointer = 0
    while instruc_pointer<len(program):
        opcode = program[instruc_pointer]
        operand =  program[instruc_pointer+1]
        a,b,c,instruc_pointer = process_instruction(opcode, operand, a,b,c, instruc_pointer)
    return res

def run():
    curr = 0
    while curr < 1000000:
        global res
        res = []
        a = curr + (787785*(8**5)+14937)*(8**4)
        b = 0
        c = 0
        instruc_pointer = 0
        while instruc_pointer<len(program):
            opcode = program[instruc_pointer]
            operand =  program[instruc_pointer+1]
            a,b,c,instruc_pointer = process_instruction(opcode, operand, a,b,c, instruc_pointer)
            # print(instruc_pointer, opcode)
            # if opcode == 3: break # one cycle
        if "2,4,1,5,7,5,4,3,1,6,0,3,5,5,3,0".startswith(','.join(list(map(str, res)))):
            print(curr, res,a)
        curr += 1
    return curr

# 7,3,5,7,5,7,4,3,0

# mods A and store in B
# 5 XOR B and store in B
# A//2**B store in C
# B^C store in B
# 6 XOR B and store in B
# A//8 and store in A
# Output B%8

# 47 [7, 3] 0
# 303 [7, 3, 5] 0
# 431 [7, 3, 5] 0
# 491 [7, 3, 5] 0
# 495 [7, 3, 5] 0
# 507 [7, 3, 5] 0

# 118928 [7, 5, 7, 4, 3, 0] 0
# 118934 [7, 5, 7, 4, 3, 0] 0
# 119440 [7, 5, 7, 4, 3, 0] 0
# 119446 [7, 5, 7, 4, 3, 0] 0
# 119755 [7, 5, 7, 4, 3, 0] 0
# 119759 [7, 5, 7, 4, 3, 0] 0
# 119761 [7, 5, 7, 4, 3, 0] 0
# 119763 [7, 5, 7, 4, 3, 0] 0
# 119766 [7, 5, 7, 4, 3, 0] 0
# 127185 [7, 5, 7, 4, 3, 0] 0
# 127190 [7, 5, 7, 4, 3, 0] 0

# 2,4,1,5,7,5,4,3,1,6,0,3,5,5,3,0


x = [303, 431, 491, 495, 507]
y = [118928, 118934, 119440, 119446, 119755, 119759, 119761, 119763, 119766, 127185, 127190]

# 2415
# 2203 [2, 4, 1, 5] 0
# 2458 [2, 4, 1, 5] 0
# 3841 [2, 4, 1, 5] 0
# 3849 [2, 4, 1, 5] 0

# 7, 5, 4, 3, 1 
# 9096 [7, 5, 4, 3, 1] 0
# 9103 [7, 5, 4, 3, 1] 0

# 30 [6, 0] 0
# 329 [6, 0, 3] 0
# 350 [6, 0, 3] 0
# 2377 [6, 0, 3, 5] 0
# 3401 [6, 0, 3, 5] 0
# 18761 [6, 0, 3, 5, 5] 0
# 26953 [6, 0, 3, 5, 5] 0
# 787785 [6, 0, 3, 5, 5, 3, 0] 0
# 788809 [6, 0, 3, 5, 5, 3, 0] 0
# 789833 [6, 0, 3, 5, 5, 3, 0] 0
# 804169 [6, 0, 3, 5, 5, 3, 0] 0
# 805193 [6, 0, 3, 5, 5, 3, 0] 0
# 812361 [6, 0, 3, 5, 5, 3, 0] 0
# 813385 [6, 0, 3, 5, 5, 3, 0] 0
# 816457 [6, 0, 3, 5, 5, 3, 0] 0
# 820553 [6, 0, 3, 5, 5, 3, 0] 0
# 821577 [6, 0, 3, 5, 5, 3, 0] 0
# 822601 [6, 0, 3, 5, 5, 3, 0] 0


# 105734774294938








        
            