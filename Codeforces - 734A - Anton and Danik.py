"""
    Codeforces - 734A - Anton and Danik
    Temática : String   
    
    Idea: Dada una cadena determinar si hay mas 'A' que 'D' o si hay 
    la misma cantidad
 
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
    ngames = input_line()
    matchs = input_line()
    frec = Counter(matchs)
    if frec['A'] > frec['D']:
       print("Anton")
    elif frec['A'] < frec['D']:
       print("Danik")
    else:
       print("Friendship")     
 
if __name__ == "__main__":
    solve()