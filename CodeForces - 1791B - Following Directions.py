"""
    CodeForces - 1791B - Following Directions

    Temática : Simulation

    Idea: 
    
    
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
        n = int(input_line())
        path = str(input_line())
        pos = [0, 0]
        find_candy = False
        for x in path:
            if x == 'U':
                pos[0] += 1
            elif x == 'D':
                pos[0] -= 1
            elif x == 'L':
                pos[1] -= 1
            elif x == 'R':
                pos[1] += 1
            if pos[0] == 1 and pos[1] == 1:
                find_candy = True

        print(("YES" if find_candy else "NO"))


if __name__ == "__main__":
    solve()
