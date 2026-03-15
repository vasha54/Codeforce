"""
    Codeforces - 1692A - Marathon

    Temática : Condicionales
    
    Idea: Dado cuatro números a,b,c y d ver cuanto son mayores que el valor
    del número a. 
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
        a,b,c,d = map(int,input_line().split())
        values = [1 for x in [b,c,d] if x > a]
        print(sum(values))

if __name__ == "__main__":
    solve()
