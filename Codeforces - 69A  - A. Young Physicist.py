"""
    Codeforces - 69A  - A. Young Physicist
    Temática : Add-Hoc   
    
    Idea: Dado una lista de vectores de tres dimensiones que indican
    las fuerzas que se aplica sobre un cuerpo y se debe determinar 
    si el cuerpo se mueve de su posición inicial (0;0;0). Si sumamos
    todos los vectores y y si el vector resultante es (0;0;0) el cuerpo
    no se mueve en caso contrario si.
 
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
    sA = sB = sC = 0
    while cases > 0:
        cases-=1
        a, b, c = map(int, input_line().split())
        sA+=a
        sB+=b
        sC+=c
    
    if sA == sB and sB==sC and sC==0:
        print("YES")
    else:
        print("NO")
 
 
if __name__ == "__main__":
    solve()