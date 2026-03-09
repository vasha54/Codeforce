"""
    Codeforces - 1742A - Sum
    Temática : Add - Hoc - Condicionales
    
    Idea: Dados tres numeros A,B y C determinar si uno de ellos es la
    suma de los otros dos
 
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
    cases = int(input_line())
    while cases > 0:
        cases = cases - 1
        A,B,C = map(int, input_line().split())
        if A + B == C or A + C == B or B + C == A:
            print("YES")
        else:
            print("NO") 
 
if __name__ == "__main__":
    solve()