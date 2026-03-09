"""
    Codeforces - 1370A - Maximum GCD
    Temática : Teoría de Numeros
    
    Idea:  Dado un valor N encontrar el mayor gcd(a,b) siendo a y b numeros
    en el rango de 1 a N. La solucion es bien simple Solo basta con dividir
    N/2 quedando con la parte entera.  
 
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
    cases = int(input_line())
    for i in range(0,cases):
        N = int(input_line().strip())
        answer = max(1,N//2)
        print(answer)     
 
if __name__ == "__main__":
    solve()