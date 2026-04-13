"""
    Codeforces - 723A - The New Year: Meeting Friends
 
    Temática : Búsqueda Exhaustiva
    
    Idea: En una linea sobre el eje X se tiene tres puntos y se quiere hallar
    la x que suma de las distancias a ese puntos entre ellos tres sea mínimo
 
"""
 
from functools import cmp_to_key, reduce
from collections import deque, Counter
 
# Comparadores en Estructuras de Datos
import heapq
import sys
import itertools
import math
 
mov_r = [2, 2, -2, -2, 1, -1, 1, -1]
mov_c = [1, -1, 1, -1, 2, 2, -2, -2]
 
MOD = 10**9 + 7
INV2 = (MOD + 1) // 2   # inverso modular de 2
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
    best = 200
    x1,x2,x3 = map(int,input_line().split())
    for i in range(1,101):
        d1 = max(i,x1) - min(i,x1) 
        d2 = max(i,x2) - min(i,x2)
        d3 = max(i,x3) - min(i,x3)
        best = min(best, d1+d2+d3)
    print(best)
 
 
if __name__ == "__main__":
    solve()
