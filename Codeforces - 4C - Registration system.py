"""
    Codeforces - 4C - Registration system
    Temática : Estructura de Datos : Diccionario   
    
    Idea: Dado un sistema de inscripción chequear si el nombre de cada equipo
    es unico o no en el momento de inscripción. En caso de existir se debe imprimir
    la cantida de equipos anteriores con ese mismo nombre. Utilizando la estructura 
    de datos de diccionario nos permite simular perfectamente el proceso.
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
MAX = 10**5
INF = 10**9

def read_nonempty():
    s = sys.stdin.readline()
    while s is not None and s.strip() == "":
        s = sys.stdin.readline()
    return s.strip()

def solve():
    input_line = read_nonempty
    inscriptions = int(input_line())
    records = {}
    while inscriptions > 0:
        inscriptions = inscriptions - 1
        name = input_line()
        ID = records.get(name,-1)
        if ID == -1:
            print("OK")
            records[name] = 1
        else:
            print(f"{name}{ID}")
            records[name] = records[name] + 1 

if __name__ == "__main__":
    solve()