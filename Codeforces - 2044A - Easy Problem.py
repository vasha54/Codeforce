"""
    Codeforces - 2044A - Easy Problem
    Temática : Add -Hoc    
    
    Idea: Dado un valor N se quiere saber la cantidad de pares de enteros postivos
    (a,b) cumplen la condición de que a = N - B. La cantidad de pares que cumplen
    la condición es N-1 
"""
 
from functools import cmp_to_key, reduce
from collections import deque, Counter
 
# Comparadores en Estructuras de Datos
import heapq
import sys
import itertools
 
mov_r = [2, 2, -2, -2, 1, -1, 1, -1]
mov_c = [1, -1, 1, -1, 2, 2, -2, -2]
 
MOD = 10**9 + 7
MAX = 510
INF = 10**9

dp = [[0] * (MAX) for _ in range(MAX)]



def read_nonempty():
    s = sys.stdin.readline()
    while s is not None and s.strip() == "":
        s = sys.stdin.readline()
    return s.strip()

def solve():
    input_line = read_nonempty
    cases = int(input_line())
    while cases > 0:
        cases = cases -1
        n = int(input_line())
        print(n-1)

if __name__ == "__main__":
    solve()