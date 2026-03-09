"""
    Codeforces - 1742B - Increasing
    Temática : Ordenamiento
    
    Idea: Dada una colección de valores saber si se pueden ordenar de tal forma
    cada elemento es estrictamente menor que el siguiente y mayor al valor anterior.
    Con solo ordenar y comprobar por cada elemento se cumpla que Ai-1 < Ai < Ai+1
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
        n = int(input_line())
        values = list(map(int,input_line().strip().split()))
        values.sort()
        valid = True
        for i in range(1,n):
            if values[i-1] >= values[i]:
                valid = False
        print(("YES" if valid else "NO"))

if __name__ == "__main__":
    solve()