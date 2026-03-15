"""
    Codeforces - 492A - Vanya and Cubes
    Temática : Aritemtica - Algebra + Busqueda Completa
    
    Idea: El problema: Vanya tiene n cubos. Quiere construir una pirámide donde 
    el nivel i (empezando desde arriba) tiene 1+2+...+i cubos. Es decir, el 
    primer nivel tiene 1, el segundo tiene 1+2=3, el tercero tiene 1+2+3=6, 
    etc. Quiere saber la máxima altura (número de niveles) que puede construir 
    con esos n cubos.

    Entonces, la cantidad total de cubos necesarios para una pirámide de altura 
    h es la suma de los primeros h números triangulares: T(1) + T(2) + ... + T(
    h) donde T(i) = i*(i+1)/2. La suma de los primeros h números triangulares 
    es igual a h*(h+1)*(h+2)/6. Se puede demostrar. Pero también podemos iterar 
    acumulando.

    Dado que n ≤ 10^4, podemos simplemente iterar hasta que la suma exceda n. 
    Pero también podemos precalcular todas las sumas para h desde 1 hasta, 
    digamos, un máximo tal que la suma no exceda 10^4. El máximo h tal que 
    h*(h+1)*(h+2)/6 ≤ 10000. Aproximadamente h^3/6 ≈ 10000 => h^3 ≈ 60000 => h 
    ≈ 39. Entonces con h=39 la suma es 39*40*41/6 = (39*40*41)/6 = (
    39*40*41)/6. 40/6 no es entero, calculemos: 39*40=1560, 1560*41=63960, /6=10660, eso es mayor que 10000. Para h=38: 38*39*40/6 = (38*39*40)/6 = 
    38*39*40/6 = 38*39*(40/6) pero mejor: 38*39=1482, 1482*40=59280, /6=9880, 
    que es menor. Entonces h máxima posible es 38. Por lo tanto podemos 
    precalcular un arreglo de sumas para h=0..38 (o hasta 40 por seguridad) y 
    luego para cada n buscar el mayor h tal que suma[h] ≤ n.
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
    gauss = [ (x * (x + 1)) // 2 + x for x in range(0,MAX+1)]
    n = int(input_line())
    blocks = 0
    heigth = 0
    while True:
        heigth += 1
        blocks += heigth * (heigth + 1) // 2
        if blocks > n:
            print(heigth - 1)
            break

if __name__ == "__main__":
    solve()