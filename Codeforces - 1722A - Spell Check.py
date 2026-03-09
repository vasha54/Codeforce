"""
    Codeforces - 1722A - Spell Check
    Temática : String + Permutación
    
    Idea: Dada una palabra verificar que es una permutación de la palabra 
    'Timur'
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

def read_nonempty():
    s = sys.stdin.readline()
    while s is not None and s.strip() == "":
        s = sys.stdin.readline()
    return s.strip()

def solve():
    input_line = read_nonempty
    word = "Timur"
    permutations = [''.join(p) for p in itertools.permutations(word)]
    cases = int(input_line())
    while cases > 0:
        cases = cases - 1
        n = int (input_line())
        name = input_line()
        if name in permutations:
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    solve()