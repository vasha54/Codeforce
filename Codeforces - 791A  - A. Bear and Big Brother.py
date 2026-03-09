"""
    Codeforces - 791A  - A. Bear and Big Brother
    Temática : Simulación   
    
    Idea: Dados lo valores A y B hallar el primer X que haga que 
    la expresión A* 3^X > B * 2^X . Con simular la situación iterando por c
    ada posible de X es sufiente para hallar la solución
 
 
 
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
    line = input_line()
    a, b = map(int, line.split())
    exponent = 0 
    while a * 3**exponent <= b * 2**exponent:
        exponent+=1
    print(exponent)
    
 
 
if __name__ == "__main__":
    solve()