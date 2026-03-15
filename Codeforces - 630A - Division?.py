"""
    Codeforces - 630A - Division?

    Temática : Implementation condicionales
    
    Idea: Dado el rating de un competidor en Codeforces determinar en que 
    división le corresponde.
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
MAX = 10**4
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
        cases -= 1
        rating = int(input_line())
        division = 0
        if rating <= 1399:
            division = 4
        elif 1400 <= rating and rating <= 1599:
            division = 3
        elif 1600 <= rating and rating <=1899:
            division = 2
        elif 1900 <= rating:
            division = 1
        print(f"Division {division}")

if __name__ == "__main__":
    solve()
