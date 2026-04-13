"""
    Codeforces - 579A - Raising Bacteria
 
    Temática : Sistema de numeración
    
    Idea: Dado un valor n determinar la cantidad de bits activo en su representación 
    en binario
 
"""
 
from functools import cmp_to_key, reduce
from collections import deque, Counter
 
# Comparadores en Estructuras de Datos
import heapq
import sys
import itertools
import math
 
mov_r = [2, 2, -2, -2, 1, -1, 1, -1]
mov_c = [1, -1, 1, -1, 2, 2, -2, -2]
 
MOD = 10**9 + 7
INV2 = (MOD + 1) // 2   # inverso modular de 2
MAX = 10**6+10
INF = 10**9
# dp = [[0]*(MAX+5) for _ in range((MAX+5))]
 
def read_nonempty():
    s = sys.stdin.readline()
    while s is not None and s.strip() == "":
        s = sys.stdin.readline()
    return s.strip()
 
 
 
def solve():
    input_line = read_nonempty
    n = int(input_line())
    bits_active = 0
    for i in range(0, 64):
        active =  n & (2**i)
        if active:
            bits_active+=1
    print(bits_active)
 
if __name__ == "__main__":
    solve()
