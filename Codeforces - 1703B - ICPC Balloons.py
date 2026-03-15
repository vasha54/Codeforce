"""
    Codeforces - 1703B - ICPC Balloons

    Temática : String
    
    Idea: Dada una cadena que representa la cantidad globos entregados en la
    competencia donde cada letra representa el problema resuelto por uno de 
    los equipos ysi se sabe que la primera vez que se resuelve el problema
    se entrega el globo adicional por lo que la solución al problema es bien
    sencilla:
      cantidad de letras + cantidad de letras unicas
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
        ballons = str(input_line())
        total_ballons = n + len(set(ballons))
        print(total_ballons)

if __name__ == "__main__":
    solve()
