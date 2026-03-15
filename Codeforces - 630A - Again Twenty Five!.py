"""
    Codeforces - 630A - Again Twenty Five!

    Temática : Aritmetica-Algebra
    
    Idea: Dado un valor n imprimir los dos ultimos dos dígitos de 5^n que siempre será el 25
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
    n = int(input_line())
    print(25)


if __name__ == "__main__":
    solve()
