"""
    Codeforces - 116A - George and Accommodation

    Temática : Busqueda Exhaustiva
    
    Idea: Dadas la cantidad de habitaciones y la cantidad de personas que viven
    en cada una habiatación asi como la capacidad de cada una debemos calcular 
    cuantas habitaciones tiene una disponibilidad de 2 o mas vacantes

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
    nrooms = int(input_line())
    answer = 0
    for _ in range(nrooms):
        life, capacity = map(int,input_line().split())
        if capacity - life >= 2:
            answer+=1
    print(answer)


if __name__ == "__main__":
    solve()
