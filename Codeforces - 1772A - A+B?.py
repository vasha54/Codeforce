"""
    Codeforces - 1772A - A+B?
    Temática : Add-Hoc + Implementación
    
    Idea: Dada una expresión de la forma a+b donde a y b son valores de un digito
    imprimir el resultado.
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
        sums = input_line()
        print(eval(sums))


if __name__ == "__main__":
    solve()