"""
    CodeForces - 2044B - Normal Problem

    Temática : String 

    Idea: Dada una cadena invertirla y sustituir todas las ocurrecias de p por q y viceversa
    
    
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
        cases -= 1
        a = list(input_line())
        a_invertida = a[::-1]
        resultado = []
        for c in a_invertida:
            if c == 'p':
                resultado.append('q')
            elif c == 'q':
                resultado.append('p')
            else:
                resultado.append('w')

        b = ''.join(resultado)
        print(b)


if __name__ == "__main__":
    solve()
