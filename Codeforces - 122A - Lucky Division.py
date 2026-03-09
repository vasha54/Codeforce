"""
    Codeforces - 122A - Lucky Division
    Temática : Teoría de Números
    
    Idea:  Dado un numero determinar si existe un divisor del numero que solo
    tenga en su representación decimal solo digitos 4 y 7
 
"""
from functools import cmp_to_key, reduce
from collections import deque, Counter
 
# Comparadores en Estructuras de Datos
import heapq
import sys
 
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
    divisors = [4, 7, 44, 47, 74, 77, 444, 447, 474, 477, 744, 747, 774, 777]
    N = int(input_line())
    exist = False
    for x in divisors:
        if N % x == 0:
            exist = True 
    print(("YES" if exist else "NO"))

if __name__ == "__main__":
    solve()
