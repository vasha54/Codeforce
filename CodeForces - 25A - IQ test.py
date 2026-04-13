"""
    CodeForces - 25A - IQ test

    Temática : Teoría de Números

    Idea: Dado un listado de numeros saber cual tiene la paridad diferente al resto.
        
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
    n = int(input_line())
    numbers = list(map(int, input_line().split()))
    evens = []
    odds = []
    for i in range(0, len(numbers)):
        evens.append(i+1) if numbers[i] % 2 == 0 else odds.append(i+1)
    print(evens[0]) if len(evens) == 1 else print(odds[0])


if __name__ == "__main__":
    solve()
