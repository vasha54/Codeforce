"""
    Codeforces - 581A - Remove Smallest

    Temática : Ordenamiento
    
    Idea: Dada una colección de valores ver si se puede dejar la colección en 
    un solo valor aplicando una o varias veces la siguiente operación:
        - Dado dos indices i y j y la diferencia entre los valores [i] y [j] es
        menor que 1.
    Con ordenar la colección y chequear que cada valor sus adyacentes su 
    diferencia cumple con las restricciones.

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
        n = int(input_line())
        values = list(map(int,input_line().split()))
        values.sort()
        is_posible = True
        for i in range(0,n-1):
            if values[i+1] - values[i] > 1:
                is_posible = False
        print(("YES" if is_posible else "NO"))


if __name__ == "__main__":
    solve()
