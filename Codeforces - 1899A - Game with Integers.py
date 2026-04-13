"""
    Codeforces - 1899A - Game with Integers
 
    Temática : Teoría de Juego
    
    Idea: Vanya gana si puede hacer que sea divisible por 3 justo después de su movimiento.
    Si n mod 3 = 1, Vanya resta 1 y gana en la primera jugada. Si 2 mod 3 = 2, Vanya suma 1 
    y gana en la primera jugada. Si n mod 3 = 0, cualquier movimiento de Vanya deja el número 
    congruente a 1 o 2 modulo 3; Vanya no puede ganar en su primer movimiento y, jugando óptimamente, 
    Vova puede evitar que Vanya consiga un múltiplo de 3 en cualquiera de las siguientes 4 jugadas 
    de Vanya dentro del límite de 10 movimientos. Por tanto en este caso gana Vova.
    Conclusión: si n mod 3 = 0 imprime Second, en caso contrario imprime First.
 
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
    cases = int(input_line())
    while cases > 0:
        cases -= 1
        n = int(input_line())
        print(("Second" if n % 3 == 0 else "First"))
        
if __name__ == "__main__":
    solve()
