"""
    Codeforces - 1669B - Triple

    Temática : Busqueda
    
    Idea: Dada una serie de valores buscar cualquier valor que se repita mas de 
    tres veces

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
        cases -= 1
        n = int(input_line())
        values = list(map(int,input_line().split()))
        values.sort()
        find = -1
        for i in range(1,n-1):
            if values[i-1] == values[i] and values[i] == values[i+1]:
                find = values[i]
                break
        print(find)


if __name__ == "__main__":
    solve()
