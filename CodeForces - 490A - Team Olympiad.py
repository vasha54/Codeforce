"""
    CodeForces - 490A - Team Olympiad

    Temática : Busqueda + Greedy

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
    nchilds = int(input_line())
    childs = list(map(int, input_line().split()))

    ones = []
    twos = []
    threes = []

    for i in range(0, len(childs)):
        if childs[i] == 1:
            ones.append(i+1)
        elif childs[i] == 2:
            twos.append(i+1)
        elif childs[i] == 3:
            threes.append(i+1)

    minimun_teams = min([len(ones), len(twos), len(threes)])

    print(minimun_teams)

    for i in range(0, minimun_teams):
        print(ones[i], twos[i], threes[i])


if __name__ == "__main__":
    solve()
