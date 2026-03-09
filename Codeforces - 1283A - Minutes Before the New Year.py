"""
    Codeforces - 1283A - Minutes Before the New Year
    Temática : Simulacion
    
    Idea: Dada una hora en formato militar calcular la cantidad de minutos que faltan
    para llegar a las 24:00
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
    cases = int(input_line())
    while cases > 0:
        cases = cases - 1
        hour, minutes = map(int,input_line().strip().split())
        times = 0
        while hour != 24 or minutes != 0:
            times = times + 1
            minutes = minutes + 1
            if minutes == 60:
                hour = hour + 1
                minutes = 0
        print(times)


if __name__ == "__main__":
    solve()