"""
    Codeforces - 580A - Kefa and First Steps

    Temática : Programación Dinámica

    Idea: Dada una colección de valores encontrar la subsecuencia de mayor
    cantidad e elementos tal que sea creciente.
 
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
    n = int(input_line())
    values = list(map(int,input_line().split()))
    dp = [1 for _ in range(0,n)]
    best = 1
    for i in range(1,n):
        if values[i-1] <= values[i]:
            dp[i] += dp[i-1]
        best = max(best,dp[i]) 
    print(best)

        
if __name__ == "__main__":
    solve()
