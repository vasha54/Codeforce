"""
    Codeforces - 1926A - Vlad and the Best of Five
    Temática : String
    
    Idea:Dada una cadena de 5 caracteres de solo A y B determinar la letra con
    mayor ocurrencias
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
    cases = int(input_line())
    while cases > 0:
        cases -= 1
        sequence = str(input_line())
        frec = Counter(sequence)
        print(("A" if frec['A'] > frec['B'] else "B"))

    # cases = int(input_line())
    # while cases > 0 :
    #     cases = cases -1
    #     n,k = map(int, input_line().split())
    #     word =str(input_line())
        

if __name__ == "__main__":
    solve()