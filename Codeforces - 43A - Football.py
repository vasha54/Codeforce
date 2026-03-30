"""
    Codeforces - 43A - Football

    Temática : String + Búsqueda
    
    Idea: Dado un listado de palabras donde esta siempre dos palabras caa una 
    con determinada frecuencias de ocurrencias .Hallar que palabra tiene mayor 
    frecuencia

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
# dp = [[0]*(MAX+5) for _ in range((MAX+5))]

def read_nonempty():
    s = sys.stdin.readline()
    while s is not None and s.strip() == "":
        s = sys.stdin.readline()
    return s.strip()

def solve():
    input_line = read_nonempty
    nscores = int(input_line())
    scores = []
    while nscores > 0:
        nscores -=1
        scores.append(input_line().strip())
    frecuencys = Counter(scores)
    value, frecuency = frecuencys.most_common(1)[0]
    print(value)

if __name__ == "__main__":
    solve()
