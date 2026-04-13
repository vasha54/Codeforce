"""
    CodeForces - 270A - Fancy Fence

    Temática : Geometría

    Idea: El ángulo interior de un polígono regular de n lados es 180 * (n - 2) / n. 
    Igualando a a y despejando n se obtiene n = 360 / (180 - a). Para que exista un 
    polígono regular, n debe ser un entero mayor o igual a 3, lo cual ocurre exactamente 
    cuando 360 es divisible por (180 - a).
        
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
        angle = int(input_line())
        if 360 % (180 - angle) == 0:
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    solve()
