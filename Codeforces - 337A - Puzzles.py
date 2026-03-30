"""
    Codeforces - 337A - Puzzles

    Temática : Greedy + Sliding indows
    
    Idea: Dado una cantidad de k puzzles donde cada uno tiene una cantidad de
    piezas cada uno que pueden diferir de otros. Se quiere elecionar n puzzles
    con la condición que la diferencia de cantidad de piezas entre el puzzle de
    mayor cantidad y de menor cantidad piezas sea la mínima cantidad posible.
    Con ordenar por la cantidad de piezas de forma ascendetemente y crear una 
    ventana de k elementos e ir recorriendo todas las posibles ventanas 
    chequear en cada ventana los extremos ver que cuales generan la menor diferencias  

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



def solve():
    input_line = read_nonempty
    
    nstudents, npuzzles = map(int,input_line().split())
    pieces = list(map(int,input_line().split()))
    pieces.sort()
    best = pieces[nstudents-1] - pieces[0]
    for x in range(0,npuzzles-nstudents+1):
        best = min(best, pieces[x+nstudents-1]-pieces[x])
    print(best)

if __name__ == "__main__":
    solve()

