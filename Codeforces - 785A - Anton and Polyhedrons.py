"""
    Codeforces - 785A - Anton and Polyhedrons

    Temática : Implementación
    
    Idea: Dada una lista de figuras calcular la cantidad de caras que hay entre 
    todas las caras
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
    polyhedrons = {
        'Tetrahedron':4,
        'Cube':6,
        'Octahedron':8,
        'Dodecahedron':12,
        'Icosahedron':20,
    }

    npolyhedrons = int(input_line())
    faces = 0
    for i in range(0,npolyhedrons):
        figure = input_line()
        faces += polyhedrons[figure]
    print(faces)

if __name__ == "__main__":
    solve()
