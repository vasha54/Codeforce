"""
    Codeforces - 1760A - Medium Number

    Temática : Busqueda
    
    Idea: Dado tres números a, b y c diferentes entre sí determinar cual de los
    tres no es ni el mínimo ni el máximo.

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
    cases = int(input_line())
    while cases > 0:
        cases -= 1
        a,b,c = map(int,input_line().split())
        max_v = max([a,b,c])
        min_v = min([a,b,c])
        values = [min_v,max_v]
        for x in [a,b,c]:
            if x not in values:
               print(x) 

if __name__ == "__main__":
    solve()
