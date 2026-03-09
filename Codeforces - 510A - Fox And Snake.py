"""
    Codeforces - 510A - Fox And Snake
    Temática : Add-Hoc + Implementación
    
    Idea: Dado dos valores N y M crear una matriz donde las filas impares 
    son llenadas con el simbolo '#' mientras las filas pares no multiplos
    de 4 todas las columnas menos la última con el simbolo '.' y la última
    '#', mientras la filas pares multiplo 4 la primera columna con el simbolo
    '#' y el resto de las filas con '.'
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
MAX = 10**5
INF = 10**9

def read_nonempty():
    s = sys.stdin.readline()
    while s is not None and s.strip() == "":
        s = sys.stdin.readline()
    return s.strip()

def solve():
    input_line = read_nonempty
    rows, columns = map(int,input_line().split())
    for x in range(1, rows+1):
        row = "#"*columns
        if x % 2 == 0 and x % 4 != 0:
            row = "."*(columns-1)+"#"
        elif x % 2 == 0 and x % 4 == 0:
            row = "#"+"."*(columns-1)
        print(row)


if __name__ == "__main__":
    solve()