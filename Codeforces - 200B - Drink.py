"""
    Codeforces - 200B - Drink
    Temática : Aritmetica - Algebra
    
    Idea:  Dado un grupo de refresco de los cuales se sabe el concentrado
    de jugo en cada uno calcular el nivel o porciento de concentrado de jugo  
    cuando se mezcaln todos. 
 
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
    N = int(input_line())
    percents = [ float(x) for x in input_line().strip().split() ]
    volumen = float(N * 100)
    sums_percent = sum(percents)
    print("{:.12f}".format(sums_percent / volumen * 100))
         
 
if __name__ == "__main__":
    solve()