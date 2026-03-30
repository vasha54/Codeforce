"""
    Codeforces - 1850A - To My Critics

    Temática : Add - Hoc
    
    Idea: Dado tres números a,b y c verificar si la sumas de dos de ellos es 
    mayor o igual a 10.

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
    cases = int(input_line())
    while cases > 0:
        cases -=1
        a, b, c = map(int,input_line().split())
        if a+b >= 10 or a+c >= 10 or b+c >= 10:
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    solve()
