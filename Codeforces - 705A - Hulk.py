"""
    Codeforces - 705A - Hulk
    Temática : String + Implementación 
    
    Idea: Dado un numero crear una coleccion de frases donde las posiciones pares
    la frase 'I hate it' y las posiciones impares 'I love it' luego concatenar
    esas frases con la frase ' that '
        
"""
 
from functools import cmp_to_key, reduce
from collections import deque, Counter
 
# Comparadores en Estructuras de Datos
import heapq
import sys
 
mov_r = [2, 2, -2, -2, 1, -1, 1, -1]
mov_c = [1, -1, 1, -1, 2, 2, -2, -2]
 
MOD = 10**9 + 7

def read_nonempty():
    s = sys.stdin.readline()
    while s is not None and s.strip() == "":
        s = sys.stdin.readline()
    return s.strip()

def solve():
    input_line = read_nonempty
    n = int(input_line())
    layers = []
    for i in range(1,n+1):
        if i % 2 == 1:
            layers.append("I hate")
        else:
            layers.append("I love")

    answer = " that ".join(layers)+" it"
    print(answer)

if __name__ == "__main__":
    solve()