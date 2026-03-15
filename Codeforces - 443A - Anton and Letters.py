"""
    Codeforces - 443A - Anton and Letters

    Temática : String
    
    Idea: Dada un conjunto letras determinar la cantidad de letras diferentes
    el conjunto es dado en el siguiente formato {<x>, <x>, <x>} 
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
    set_str = str(input_line())
    if set_str == "{}":
        print(0)
    else:
        set_str = set_str[1:-1]
        set_str = set_str.split(", ")
        set_letters = set(set_str)
        print(len(set_letters))

if __name__ == "__main__":
    solve()