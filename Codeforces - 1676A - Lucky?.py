"""
    Codeforces - 1676A - Lucky?

    Temática : Implementation 
    
    Idea: Dado un número de seis digitos se quiere saber si la suma de los 
    primeros digitos es igual a la suma de los últimos tres dígitos 
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
    cases = int(input_line())
    while cases > 0:
        cases -= 1
        number = str(input_line())
        numbers = [ int(x) for x in number]
        sums_first = sum(numbers[0:3])
        sums_last  = sum(numbers[3:])
        print(("YES" if sums_first == sums_last else "NO"))

if __name__ == "__main__":
    solve()
