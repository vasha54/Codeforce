"""
    Codeforces - 1560A - Dislike of Threes

    Temática : Add - Hoc + Busqueda
    
    Idea: Dado un valor k encontrar el k-enesimo valor natural que no es 
    divisible por 3 o termina en 3.

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

    sequence = [] 
    i = 1
    while len(sequence) <= 1010:
        if i%3 != 0 and  i%10 != 3:
           sequence.append(i)
        i += 1 

    while cases > 0:
        cases -=1
        k = int(input_line())
        print(sequence[k-1])

if __name__ == "__main__":
    solve()
