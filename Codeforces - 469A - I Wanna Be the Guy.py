"""
    Codeforces - 288A - Is your horseshoe on the other hoof?

    Temática : Estructura de Datos + Set
    
    Idea: Dado un juego con su cantidad level o niveles y dos jugadores que se
    conocen los niveles o levels que pueden pasar cada uno. Se quiere saber si
    entre los dos jugadores pueden complentar todos los niveles del juego. Con
    almacenar todos los niveles que pueden pasar ambos jugadores en un set y ver
    si su longitud es igual o no a la cantidad de niveles del juego.

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
INV2 = (MOD + 1) // 2   # inverso modular de 2
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
    levels = int(input_line())
    
    line = input_line().split()
    xs = int(line[0])
    x_levels = set(map(int, line[1:1+xs])) if xs > 0 else set()

    line = input_line().split()
    ys = int(line[0])
    y_levels = set(map(int, line[1:1+ys])) if ys > 0 else set()

    all_passed = x_levels.union(y_levels)
    if len(all_passed) == levels:
        print("I become the guy.")
    else:
        print("Oh, my keyboard!")

if __name__ == "__main__":
    solve()

