"""
    Codeforces - 486A - Calculating Function
    Temática : Aritmetica - Algebra
    
    Idea: Dado un valor N se debebe hallar el valor de F(N). Donde F(N) se
    define como la suma de todos los números pares hasta N menos la suma de todos 
    los números impares hasta N.

    La suma de todos los números pares hasta N se define como X*(X+1) siendo
    X = N/2

    La suma de todos los numeros impares hasta N se define como Y^2 siendo
    Y = N/2 + (1 si N mod 2 ==1 sino 0)   
 
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
    N = int(input_line())
    X = N // 2
    Y = N // 2 + (1 if N %2 ==1 else 0)
    answer = X*(X+1) - Y**2
    print(answer)
         
 
if __name__ == "__main__":
    solve()