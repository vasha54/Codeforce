"""
    Codeforces - 1807A - Plus or Minus
    Temática : Add-Hoc 
    
    Idea: Dado los valores a,b,c determinar cual de las siguentes expresion
    es la que se cumple:
      * a + b = c Imprimir +
      * a - b = c Imprimir -
 
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
    while cases > 0:
        cases = cases - 1
        a,b,c = map(int, input_line().split())
        if a + b == c:
            print("+")
        elif a - b == c: 
            print("-")
         
 
if __name__ == "__main__":
    solve()