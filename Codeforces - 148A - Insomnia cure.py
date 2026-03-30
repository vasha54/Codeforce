"""
    Codeforces - 148A - Insomnia cure

    Temática : Combinatoria + Principio Exclusión-Inclusión
    
    Idea: El problema consiste en determinar cuántos dragones, numerados del 1 
    al d, sufren al menos uno de los cuatro posibles daños, donde un dragón es 
    dañado si su número es divisible por k, l, m o n. La solución más directa 
    sería recorrer todos los dragones y verificar cada condición, lo que resulta 
    en una complejidad O(d) perfectamente aceptable dado que d ≤ 10⁵; sin embargo, 
    el principio de inclusión‑exclusión ofrece un enfoque más elegante y de 
    tiempo constante O(1), independiente del valor de d. Este principio permite 
    calcular la cardinalidad de la unión de cuatro conjuntos (los divisibles por 
    cada uno de los cuatro números) mediante la suma de los tamaños individuales, 
    la resta de las intersecciones de a pares, la suma de las intersecciones de 
    a tres y la resta de la intersección de los cuatro. Cada cardinalidad se 
    obtiene fácilmente como el cociente entero de d entre el mínimo común múltiplo 
    (mcm) de los números involucrados, pues los números divisibles por varios 
    criterios son exactamente los múltiplos del mcm correspondiente. Gracias a 
    que los valores de k, l, m, n son muy pequeños (≤ 10), los mcm involucrados 
    son pequeños y su cálculo es trivial mediante la relación mcm(a,b)=a·b/mcd(a,b). 
    Así, el problema se resuelve con unas pocas operaciones aritméticas, lo que 
    resulta en una solución óptima en tiempo y memoria.

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
INV2 = (MOD + 1) // 2   # inverso modular de 2
MAX = 10**6+10
INF = 10**9
# dp = [[0]*(MAX+5) for _ in range((MAX+5))]

def read_nonempty():
    s = sys.stdin.readline()
    while s is not None and s.strip() == "":
        s = sys.stdin.readline()
    return s.strip()

def lcm(a, b):
    """Retorna el mínimo común múltiplo de a y b."""
    return a // math.gcd(a, b) * b

def solve():
    input_line = read_nonempty
    
    k = int(input_line())
    l = int(input_line())
    m = int(input_line())
    n = int(input_line())
    d = int(input_line())

    # Suma de conjuntos individuales
    damaged_dragons = (d // k) + (d // l) + (d // m) + (d // n)

    # Restar intersecciones de dos conjuntos
    damaged_dragons -= (d // lcm(k, l))
    damaged_dragons -= (d // lcm(k, m))
    damaged_dragons -= (d // lcm(k, n))
    damaged_dragons -= (d // lcm(l, m))
    damaged_dragons -= (d // lcm(l, n))
    damaged_dragons -= (d // lcm(m, n))

    # Sumar intersecciones de tres conjuntos
    damaged_dragons += (d // lcm(lcm(k, l), m))
    damaged_dragons += (d // lcm(lcm(k, l), n))
    damaged_dragons += (d // lcm(lcm(k, m), n))
    damaged_dragons += (d // lcm(lcm(l, m), n))

    # Restar intersección de los cuatro conjuntos
    damaged_dragons -= (d // lcm(lcm(lcm(k, l), m), n))

    print(damaged_dragons)

if __name__ == "__main__":
    solve()

