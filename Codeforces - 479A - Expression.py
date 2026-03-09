"""
    Codeforces - 479A - Expression
    Temática : Búsqueda
    
    Idea: Dado tres valores a,b,c determinar el mayor valor que puedo generar usando
    estos numeros y las operaciones de suma y multiplicación
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
    a = int(input_line())
    b = int(input_line())
    c = int(input_line())

    f = [a,b,c]
    values = [
        f[0] + f[1] + f[2],
        f[0] + f[1] * f[2],
       (f[0] + f[1]) * f[2],
        f[0] * (f[1] + f[2]),
        f[0] * f[1] * f[2],
    ]
    print(max(values))


if __name__ == "__main__":
    solve()