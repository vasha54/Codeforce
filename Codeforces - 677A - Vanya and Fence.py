"""
    Codeforces - 677A - Vanya and Fence
    Temática : String   
    
    Idea: Dada una lista de valores determinar la cantidad de elementos
    mayores a un valor dado . La respuesta es la cantidad de elementos
    de la colección más la cantidad de elementos de la misma colección
    que su valor es mayor que un valor determinado
 
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
    n,h = map(int,input_line().split())
    line = input_line()
    heights = [int(x) for x in line.split()] 
    answer = len(heights) + sum(1 for x in heights if x > h)
    print(answer)    
 
if __name__ == "__main__":
    solve()