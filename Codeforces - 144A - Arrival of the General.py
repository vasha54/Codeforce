"""
    Codeforces - 144A - Arrival of the General
 
    Temática : Búsqueda 
    
    Idea: Dado una colección de valores contar la cantidad de intercambio de
    valores adyacentes tal que en la primera posición de la colección quede
    el mayor de los valores de colección y en la ultima posición el menor valor
    de la colección. 
    Solo debemos buscar el mayor valor lo más a la izquierda posible y el menor 
    valor posible lo mas a la derecha posible y con esta posciones podemos 
    calcular cuantos intercambios se tiene que hacer para llegar al principio y 
    al final de la colección tener en cuenta que las posiciones se pueden 
    cruzar.
 
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
    n = int(input_line())
    values = list(map(int,input_line().split()))
    min_value = values[0]
    min_pos = 0
    max_pos = 0
    max_value = values[0]
    for i in range(0,n):
        if values[i] <= min_value:
            min_pos = i
            min_value = values[i]
        if values[i] > max_value:
            max_pos = i
            max_value = values[i]

    solution = max_pos + ((n-1) - min_pos)
    if max_pos > min_pos:
        solution -=1
    print(solution)

        
if __name__ == "__main__":
    solve()
