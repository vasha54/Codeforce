"""
    CodeForces - 1857A - Array Coloring

    Temática : Teoría de Números

    Idea: Dada un a coleccion de valores saber si se puede conformar dos grupos tal que la
    sumas de los elementos de cada grupo tenga la misma paridad. Con que la suma total sea par 
    es suficiente para pder construir los dos conjuntos.

        
"""

from functools import cmp_to_key, reduce
from collections import deque, Counter

# Comparadores en Estructuras de Datos
import heapq
import sys
import bisect
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
        cases = cases - 1
        n = int(input_line())
        numbers = list(map(int, input_line().split()))
        sum_total = sum(numbers)
        possible = False
        if sum_total % 2 == 0:
            possible = True
        print("YES" if possible else "NO")


if __name__ == "__main__":
    solve()
