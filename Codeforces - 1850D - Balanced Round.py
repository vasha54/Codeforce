"""
    CSES - Two Sets II
    Temática : Programación Dinámico
    
    Idea: Dada una colección de valores los cuales se pueden ordenar encontrar
    la mayor secuancia de valores que se puede tomar tal que la diferencia dentre 
    los elementos consecutivos no superen un valor k.
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
MAX = 10**5
INF = 10**9

def read_nonempty():
    s = sys.stdin.readline()
    while s is not None and s.strip() == "":
        s = sys.stdin.readline()
    return s.strip()

def solve():
    input_line = read_nonempty
    cases = int(input_line())
    while cases > 0:
        cases = cases - 1
        n,k = map(int,input_line().split())
        values = list(map(int,input_line().split()))
        values.sort()
        best = 1
        tmp = 1
        for x in range(1,n):
            if values[x] - values[x-1] <= k:
                tmp = tmp + 1
            else:
                tmp =  1
            best = max(best,tmp)
        print(n-best)


if __name__ == "__main__":
    solve()