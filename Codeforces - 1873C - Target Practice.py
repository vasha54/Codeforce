"""
    Codeforces - 1873C - Target Practice
    Temática : Matriz + Implementación   
    
    Idea: Dada Una matriz de 10x10 en forma de diana donde cada anillo rectangular
    tiene una puntuación determnada
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

# dp = [[0] * (MAX) for _ in range(MAX)]



def read_nonempty():
    s = sys.stdin.readline()
    while s is not None and s.strip() == "":
        s = sys.stdin.readline()
    return s.strip()

def f(_r,_c):
    h = min(_r-1,10-_r)+1
    v = min(_c-1,10-_c)+1
    return min(h,v)

def solve():
    input_line = read_nonempty
    cases = int(input_line())
    while cases > 0:
        cases = cases - 1
        score = 0
        for i in range(1,11):
            row = str(input_line())
            for j in range(1,11):
                if row[j-1] == 'X':
                    score = score + min(min(i-1,10-i)+1,min(j-1,10-j)+1)
        print(score)

if __name__ == "__main__":
    solve()