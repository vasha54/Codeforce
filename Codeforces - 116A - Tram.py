"""
    Codeforces - 116A - Tram

    Temática : Simulación
    
    Idea: Se tiene un tren que cubre una ruta con diferentes paradas de las cuales
    se conoce la cantidad de personas que se bajan y cuantas suben al tren. Conocido
    esto queremos saber cual debe ser la capacidad máxima del tren para que se puedan 
    transportar todos los pasajeros. Con simular el proceso y llevar en todo momento 
    la cantidad de pasajeros que lleva el tren y buscar en que momento se genera el mayor 
    valor basta para solucionar el problema.

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
    stations = int(input_line())
    capacity = 0 
    passengers = 0 
    for _ in range(stations):
        down, up = map(int,input_line().split())
        passengers -= down
        passengers += up 
        capacity = max(capacity,passengers)

    print(capacity)


if __name__ == "__main__":
    solve()
