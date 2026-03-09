"""
    Codeforces - 405A - Gravity Flip
    Temática : Ordenamiento
    
    Idea: Dado unca colección de numeros imprimir los numeros ordenamos de forma
    ascedentemente
        
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
    n = int(input_line())
    array = list(map(int,input_line().strip().split()))
    array.sort()
    for x in array:
        print(x, end=" ")
    print()

if __name__ == "__main__":
    solve()