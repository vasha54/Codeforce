"""
    Codeforces - 363B - Fence

    Temática : Programación Dinámica + Suma de prefijo
    
    Idea: Dado un array de valores encontrar el subarrary de k elemento cuya suma 
    sea mínima e imprimir el índice de inicio comenzando en cero.
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
    n, k = map(int,input_line().split())
    values = list(map(int,input_line().split()))
    values = [0] + values
    for i in range(1,n+1):
        values[i] += values[i-1]
    index = -1
    best = sum(values) * 2
    for j in range(k,n+1):
        if best > values[j] - values[j-k]:
            best = values[j] - values[j-k]
            index = j-k+1
    print(index)

if __name__ == "__main__":
    solve()
