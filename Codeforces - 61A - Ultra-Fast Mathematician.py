"""
    Codeforces - 61A - Ultra-Fast Mathematician
    Temática : Operaciones de Bit XOR (OR exclusivo).
    
    Idea:  Dada dos cadenas binarias de n bits se quiere obtener una cadena 
    de n bits donde el bit estará en 1 si en esa misma posición en las cadenas
    de las cadenas son diferentes los valores 
 
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
    a = input_line().strip()
    b = input_line().strip()
    result = []
    for i in range(len(a)):
        result.append('1' if a[i] != b[i] else '0')
    print(''.join(result))
         
 
if __name__ == "__main__":
    solve()