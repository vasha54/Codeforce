"""
    Codeforces - 427A - Police Recruits

    Temática : Simulación
    
    Idea: Si simulamos el proceso como se nos describe el problema podemos 
    perfectamente encontrar la solución.

"""
 
from functools import cmp_to_key, reduce
from collections import deque, Counter
 
# Comparadores en Estructuras de Datos
import heapq
import sys
import itertools
import math
 
mov_r = [2, 2, -2, -2, 1, -1, 1, -1]
mov_c = [1, -1, 1, -1, 2, 2, -2, -2]
 
MOD = 10**9 + 7
INV2 = (MOD + 1) // 2   # inverso modular de 2
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
    
    nevents = int(input_line())
    polices = 0
    crimes_untreated = 0
    events = list(map(int,input_line().split()))
    for x in events:
        if x == -1:
            if polices > 0:
                polices -=1
            else:
                crimes_untreated +=1
        else:
            polices += x
    print(crimes_untreated)



if __name__ == "__main__":
    solve()

