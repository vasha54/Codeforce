"""
    Codeforces - 313A - Ilya and Bank Account

    Temática : Implementación + String
    
    Idea: 

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
MAX = 10**6+10
INF = 10**9
# dp = [[0]*(MAX+5) for _ in range((MAX+5))]

def read_nonempty():
    s = sys.stdin.readline()
    while s is not None and s.strip() == "":
        s = sys.stdin.readline()
    return s.strip()

def solve():
    input_line = read_nonempty
    n = int(input().strip())
    s = str(n)
    best = n
    best = max(best, int(s[:-1]))
    best = max(best, int(s[:-2] + s[-1]))
    print(best)

if __name__ == "__main__":
    solve()
