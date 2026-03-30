"""
    Codeforces - 136A - Even Odds
    
    Temática : Aritmetica - Algebra
    
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
    nchilds = int(input_line())
    p_childs = list(map(int,input_line().split()))
    q_childs = [0 for _ in range(nchilds)]
    for i in range(0,nchilds):
        q_childs[p_childs[i]-1] = str(i+1)

    print(" ".join(q_childs))  

if __name__ == "__main__":
    solve()
