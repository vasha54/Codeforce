"""
    Codeforces - 1294A - Collecting Coins

    Temática : Aritmetica - Álgebra

    Idea: Dado 4 valores A, B, C, y D se quiere saber si se puede distribuir el 
    valor de D en d1, d2 y d3 tal que se cumpla lo siguiente:
    - A + d1 == B + d2 == C + d3
    - d1 + d2 + d3 == D
 
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
MODM1 = MOD - 1          # para exponentes
MOD2M1 = 2 * MODM1       # para reducir d(N) antes de dividir por 2

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
    cases = int(input_line())
    while cases > 0:
        cases-=1
        a,b,c,n = map(int,input_line().split())
        l = [a,b,c]
        l.sort()
        d = (l[2]-l[0]) + (l[2]-l[1])

        if d > n:
            print("NO")
        else:
            n-=d
            print(("YES" if n%3==0 else "NO"))


        
if __name__ == "__main__":
    solve()
