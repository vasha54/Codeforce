"""
    Codeforces - 1475A - Odd Divisor
    Temática : Teoría de Numeros 
    
    Idea: Dado un número determinar si tiene un divisor impar mayor
    que 1. Los únicos números que no lo cumplen son los números que sean
    potencias de 2.
 
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

def check(_x):
    while _x % 2 == 0:
        _x = _x // 2
    return True if _x > 1 else False

def solve():
    input_line = read_nonempty
    cases = int(input_line())
    while cases > 0:
        cases = cases - 1
        A = int(input_line())
        if check(A):
            print("YES")
        else:
            print("NO") 
 
if __name__ == "__main__":
    solve()