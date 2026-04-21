"""
    CodeForces - 1360A - Minimal Square

    Temática : Aritmetica - Algebra 

    Idea: Se nos pide encontrar el área mínima de un terreno cuadrado que pueda 
    contener dos rectángulos idénticos de dimensiones a x b. Los rectángulos se 
    pueden rotar (usar a x b o b x a), mover y deben tener sus lados paralelos a l
    os lados del cuadrado. No pueden solaparse, pero sí tocarse.
    
    Dado que solo hay dos rectángulos, las configuraciones óptimas son muy limitadas. 
    Para cada posible orientación de los rectángulos (ambos iguales o diferentes), 
    la colocación más compacta se logra alineándolos lado a lado o apilándolos, 
    ya que cualquier disposición que evite el solapamiento fuerza que las proyecciones 
    en el eje X o en el eje Y sean disjuntas. Deslizándolos contra los bordes se obtiene 
    un cuadrado de lado igual al máximo del ancho y alto totales.

    S = min( max(2a, b), max(a, 2b), max(2b, a), max(b, 2a) )
        
"""

from functools import cmp_to_key, reduce
from collections import deque, Counter

# Comparadores en Estructuras de Datos
import heapq
import sys
import bisect
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
    cases = int(input_line())
    while cases > 0:
        cases = cases - 1
        a, b = map(int, input_line().split())
        sides = min(max(2*a, b), max(a, 2*b), max(2*b, a), max(b, 2*a))
        print(sides**2)


if __name__ == "__main__":
    solve()
