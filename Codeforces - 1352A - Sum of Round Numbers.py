"""
    Codeforces - 1352A - Sum of Round Numbers
 
    Temática : Sistema de numeración
    
    Idea: Dado un numero expresarlo como suma de de sumandos que se forman
    bajo la regla x10^n .
 
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
MODM1 = MOD - 1          # para exponentes
MOD2M1 = 2 * MODM1       # para reducir d(N) antes de dividir por 2

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
    cases = int(input_line())
    while cases > 0:
        cases -= 1
        n = int(input_line())
        exp = 0
        fact = []
        while n > 0:
            d = n % 10
            n = n // 10
            if d:
                fact.append(str(d*(10**exp)))
            exp +=1
        print(len(fact))
        print(" ".join(fact))
        
if __name__ == "__main__":
    solve()
