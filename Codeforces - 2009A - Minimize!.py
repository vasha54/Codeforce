"""
    Codeforces - 2009A - Minimize!

    Temática : Busqueda Exhaustiva
    
    Idea: Dado los valores a y b buscar un valor k que es igual a (c-a)+ (b-c)
    donde c esta entre a y b

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
# dp = [[0]*(MAX+5) for _ in range((MAX+5))]

def read_nonempty():
    s = sys.stdin.readline()
    while s is not None and s.strip() == "":
        s = sys.stdin.readline()
    return s.strip()

def solve():
    input_line = read_nonempty
    cases = int(input_line())

    while cases > 0:
        cases -=1
        a,b = map(int,input_line().split())
        print(b-a)

if __name__ == "__main__":
    solve()
