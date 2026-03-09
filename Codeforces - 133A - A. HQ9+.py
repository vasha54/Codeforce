"""
    Codeforces - 133A - A. HQ9+
    Temática : String
    
    Idea: Dada una cadena de letras verificar si en la cadena existe
    al menos uno de los siguientes caracteres: H,9 y Q
 
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
    source = input_line()
    caracters = ('9', 'Q', 'H') 
    if any(c in source for c in caracters):
        print("YES")
    else:
        print("NO")
 
if __name__ == "__main__":
    solve()